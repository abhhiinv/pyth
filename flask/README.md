# Flask Task Manager - To-Do List Application

A beautiful, responsive web application for managing tasks built with Flask and pure CSS.

## 📁 Project Structure

```
flask-task-manager/
│
├── app.py                      # Main Flask application
├── database.py                 # Dummy database implementation
├── requirements.txt            # Python dependencies
│
└── templates/
    ├── base.html              # Base template with Jinja2 inheritance
    ├── index.html             # Home page - display and add tasks
    └── edit.html              # Edit task page
```

## ✨ Features

### Task Model
- **id**: Primary key (auto-incremented integer)
- **content**: Task description (string)
- **completed**: Task status (0 = incomplete, 1 = complete)

### CRUD Operations
1. **Create**: Add new tasks via POST request at `/add`
2. **Read**: View all tasks on the home page (`/`)
3. **Update**: 
   - Toggle task completion status at `/toggle/<task_id>`
   - Edit task content at `/edit/<task_id>`
4. **Delete**: Remove tasks at `/delete/<task_id>`

### Additional Features
- ✅ Flash messages for user feedback
- 🎨 Beautiful gradient design with smooth animations
- 📱 Fully responsive mobile-first design
- 🔄 Real-time task status updates
- 💾 Persistent dummy database (in-memory)
- ⚡ Fast and lightweight

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Create Project Directory
```bash
mkdir flask-task-manager
cd flask-task-manager
```

### Step 2: Set Up File Structure
Create the following files with their respective content:
- `app.py`
- `database.py`
- `requirements.txt`

Create a `templates` folder and add:
- `templates/base.html`
- `templates/index.html`
- `templates/edit.html`

### Step 3: Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

## 🎯 Running the Application

### Option 1: Using Python directly
```bash
python app.py
```

### Option 2: Using Flask command
```bash
# On Windows
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

# On macOS/Linux
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The application will start on `http://127.0.0.1:5000/`

## 📖 Usage Guide

### Adding a Task
1. Enter your task in the input field on the home page
2. Click "Add Task" button
3. You'll see a success message and the task will appear in the list

### Completing a Task
1. Click the "✓ Complete" button next to any task
2. The task will be marked with a strikethrough and green background
3. Click "↩️ Undo" to mark it as incomplete again

### Editing a Task
1. Click the "✏️ Edit" button next to any task
2. Modify the task content in the edit form
3. Click "💾 Save Changes" to update, or "✖️ Cancel" to go back

### Deleting a Task
1. Click the "🗑️ Delete" button next to any task
2. Confirm the deletion in the popup dialog
3. The task will be permanently removed

## 🎨 Design Features

- **Purple Gradient Theme**: Modern purple gradient color scheme
- **Smooth Animations**: Hover effects and transitions
- **Mobile Responsive**: Works perfectly on phones, tablets, and desktops
- **User Feedback**: Flash messages for all actions
- **Clean UI**: Minimalist and intuitive interface

## 🛠️ Technical Details

### Database Implementation
This application uses a **dummy in-memory database** implemented with Python lists:
- Tasks are stored in a global list variable
- Data persists only during the application runtime
- Perfect for learning and development
- In production, replace with SQLite, PostgreSQL, or MySQL

### Flask Routes
- `GET /` - Display all tasks (index page)
- `POST /add` - Create a new task
- `GET /toggle/<task_id>` - Toggle task completion status
- `GET /delete/<task_id>` - Delete a task
- `GET /edit/<task_id>` - Display edit form
- `POST /edit/<task_id>` - Update task content

### Template Inheritance
The application uses Jinja2 template inheritance:
- `base.html`: Contains common structure, header, and styles
- `index.html`: Extends base, shows task list and add form
- `edit.html`: Extends base, shows edit form

## 🔧 Customization

### Changing Colors
Edit the CSS gradients in the `<style>` sections:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Adding More Fields
1. Update the task model in `database.py`
2. Modify the forms in `index.html` and `edit.html`
3. Update the database functions to handle new fields

### Switching to Real Database
Replace `database.py` with SQLAlchemy models:
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
```

## 📝 Notes

- The secret key in `app.py` should be changed in production
- This is a learning project - not production-ready
- Data is lost when the server restarts (in-memory storage)
- For production use, implement a real database and add authentication

## 🎓 Learning Outcomes

This project demonstrates:
- Flask application structure
- Routing and HTTP methods (GET, POST)
- Template inheritance with Jinja2
- Form handling and validation
- Flash messages for user feedback
- CRUD operations
- CSS styling and responsive design
- RESTful routing patterns

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project for learning Flask web development!

---

**Happy Task Managing! 📝✨**
