# Dummy database implementation using Python lists
# In a real application, you would use SQLite, PostgreSQL, or another database

# Global variable to store tasks (this acts as our dummy database)
tasks_db = []

# Counter for task IDs
task_id_counter = {'current': 1}

def init_db():
    """Initialize the database with some sample tasks"""
    global tasks_db, task_id_counter

    # Clear existing data
    tasks_db = []
    task_id_counter['current'] = 1

    # Add some sample tasks
    sample_tasks = [
        {'id': 1, 'content': 'Learn Flask framework', 'completed': 0},
        {'id': 2, 'content': 'Build a To-Do application', 'completed': 0},
        {'id': 3, 'content': 'Deploy the application', 'completed': 0}
    ]

    tasks_db.extend(sample_tasks)
    task_id_counter['current'] = 4

    print("Database initialized with sample tasks!")

def get_all_tasks():
    """Retrieve all tasks from the database"""
    return tasks_db

def add_task(content):
    """Add a new task to the database"""
    new_task = {
        'id': task_id_counter['current'],
        'content': content,
        'completed': 0
    }
    tasks_db.append(new_task)
    task_id_counter['current'] += 1
    return new_task

def get_task_by_id(task_id):
    """Get a single task by its ID"""
    for task in tasks_db:
        if task['id'] == task_id:
            return task
    return None

def toggle_task_status(task_id):
    """Toggle the completed status of a task"""
    task = get_task_by_id(task_id)
    if task:
        task['completed'] = 1 if task['completed'] == 0 else 0
        return True
    return False

def update_task(task_id, new_content):
    """Update the content of a task"""
    task = get_task_by_id(task_id)
    if task:
        task['content'] = new_content
        return True
    return False

def delete_task(task_id):
    """Delete a task from the database"""
    global tasks_db
    for i, task in enumerate(tasks_db):
        if task['id'] == task_id:
            tasks_db.pop(i)
            return True
    return False
