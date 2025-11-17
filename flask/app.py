from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, get_all_tasks, add_task, toggle_task_status, delete_task, get_task_by_id, update_task

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Initialize the database when the app starts
init_db()

@app.route('/')
def index():
    """Display all tasks on the home page"""
    tasks = get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    """Add a new task"""
    content = request.form.get('content')

    if content and content.strip():
        add_task(content.strip())
        flash('Task added successfully!', 'success')
    else:
        flash('Task content cannot be empty!', 'error')

    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    """Toggle the completed status of a task"""
    success = toggle_task_status(task_id)

    if success:
        flash('Task status updated!', 'success')
    else:
        flash('Task not found!', 'error')

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    """Delete a task"""
    success = delete_task(task_id)

    if success:
        flash('Task deleted successfully!', 'success')
    else:
        flash('Task not found!', 'error')

    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    """Edit an existing task"""
    if request.method == 'POST':
        content = request.form.get('content')

        if content and content.strip():
            success = update_task(task_id, content.strip())
            if success:
                flash('Task updated successfully!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Task not found!', 'error')
        else:
            flash('Task content cannot be empty!', 'error')

    task = get_task_by_id(task_id)
    if task:
        return render_template('edit.html', task=task)
    else:
        flash('Task not found!', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
