from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Add new task
        task_content = request.form['content']
        due_date_str = request.form.get('due_date')
        completed = 'completed' in request.form
        
        new_task = Task(content=task_content, completed=completed)
        if due_date_str:
            new_task.due_date = date.fromisoformat(due_date_str)
        
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    # Get sort parameter from URL (GET request)
    sort_by = request.args.get('sort', 'default')

    # Define tasks based on sort (THIS MUST COME BEFORE ANY PRINT)
    if sort_by == 'due_asc':
        tasks = Task.query.order_by(Task.due_date.asc().nulls_last()).all()
    elif sort_by == 'due_desc':
        tasks = Task.query.order_by(Task.due_date.desc().nulls_first()).all()
    else:
        tasks = Task.query.order_by(Task.id.desc()).all()

    # Now it's safe to print for debugging
    print(f"Sort by: {sort_by}")
    print([t.due_date for t in tasks])  # This will show list of due dates

    today = date.today()

    return render_template('index.html', tasks=tasks, today=today)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        task.completed = 'completed' in request.form
        due_date_str = request.form .get('due_date')
        if due_date_str:
            task.due_date = date.fromisoformat(due_date_str)
        else:
            task.due_date = None
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', task = task)

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
def toggle(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))

if __name__== '__main__':
    app.run(debug = True)
