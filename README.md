# Flask-Task-Manager-Web-App

# Flask Task Manager Web App

 - A full-stack task management application built with **Python Flask**, **SQLite**, **SQLAlchemy**, **Bootstrap 5**, and   **Jinja2** templating.  
 - Allows users to **create, read, update, delete** tasks, mark them as completed, set due dates, and sort by priority.

     1. ### Features
      - **Full CRUD operations** for tasks
      - **Task completion** with checkbox and visual strikethrough
      - **Due date** support with calendar picker
      - **Overdue task highlighting** (red warning)
      - **Dynamic sorting** by:
      - Added date (newest first – default)
      - Due date (soonest first)
      - Due date (latest first)
      - Responsive and modern UI using **Bootstrap 5**
      - Persistent data storage with **SQLite** database

    2. ### Tech Stack
     - **Backend**: Python, Flask, SQLAlchemy
     - **Database**: SQLite
     - **Frontend**: HTML5, CSS3, Bootstrap 5, Jinja2 templating
     - **Other**: datetime handling, form validation, dynamic routing

    3. ### Project Screenshots
      (Add 3–5 screenshots here – recommended:  
       i). Empty task list  
      ii). Tasks with due dates & completed items  
     iii). Sorting dropdown in action
      iv). Edit page with date picker & checkbox)

    4. ### How to Run Locally
       
     i). Clone the repository:
         ```bash
      git clone https://github.com/yashraj022381/flask-task-manager.git
        cd flask-task-manager
   
     ii). Create & activate virtual environment:Bashpython -m venv venv
          venv\Scripts\activate   # Windows
          source venv/bin/activate   # Mac/Linux

    iii). Install dependencies:
          Bash
          pip install flask flask-sqlalchemy

    iv). Run the application:
         Bash
         python app.py

     v). Open in browser:
         http://127.0.0.1:5000/

    5. Folder Structure
      textflask-task-manager/
      ├── app.py                # Main Flask application
      ├── tasks.db              # SQLite database (auto-generated)
      ├── templates/
      │   ├── index.html        # Main task list page
      │   └── update.html       # Edit task page
      └── README.md
