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
        # Add new task (your existing code)
        task_content = request.form['content']
        due_date_str = request.form.get('due_date')
        completed = 'completed' in request.form
        
        new_task = Task(content=task_content, completed=completed)
        if due_date_str:
            new_task.due_date = date.fromisoformat(due_date_str)
        
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    # Get search query and sort preference from GET request
    search_query = request.args.get('search', '').strip()
    sort_by = request.args.get('sort', 'default')

    # Build base query
    query = Task.query

    # Apply search filter (case-insensitive partial match)
    if search_query:
        query = query.filter(Task.content.ilike(f"%{search_query}%"))

    # Apply sorting
    if sort_by == 'due_asc':
        query = query.order_by(Task.due_date.asc().nulls_last())
    elif sort_by == 'due_desc':
        query = query.order_by(Task.due_date.desc().nulls_first())
    else:
        query = query.order_by(Task.id.desc())

    tasks = query.all()

    today = date.today()

    # Optional debug prints (remove later)
    # print(f"Search: '{search_query}' | Sort by: {sort_by}")
    # print([t.content for t in tasks])

    return render_template('index.html', 
                          tasks=tasks, 
                          today=today,
                          search_query=search_query)  # pass back for input value

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
