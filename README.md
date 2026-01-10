# Task-Manager-Web-App


 - A full-stack task management application built with **Python Flask**, **SQLite**, **SQLAlchemy**, **Bootstrap 5**, and   **Jinja2** templating.  
 - Allows users to **create, read, update, delete** tasks, mark them as completed, set due dates, and sort by priority.

   1. ### Key Features
     - Create, read, update, delete (CRUD) tasks
     - Mark tasks as completed (checkbox + strikethrough visual feedback)
     - Set due dates with calendar picker
     - Highlight overdue tasks in red
     - Sort tasks by:
       - Added date (newest first – default)
       - Due date (soonest first)
       - Due date (latest first)
     - Search tasks by keyword (case-insensitive partial match)
     - Responsive and modern UI using Bootstrap 5
     - Persistent storage with SQLite database

   2. ### Tech Stack
     - **Backend**: Python, Flask, SQLAlchemy
     - **Database**: SQLite
     - **Frontend**: HTML5, CSS3 (Bootstrap 5), Jinja2 templating
     - **Other**: datetime handling, form validation, dynamic queries (.order_by, .filter)

   3. ### Project Screenshots:
      
       i). Empty task list:
           ![Image](https://github.com/user-attachments/assets/8001eb20-ab59-4ce6-8873-204c84802db4)
      
      ii). Tasks with due dates & completed items:
           ![Image](https://github.com/user-attachments/assets/02db3058-ef21-402a-967d-5164d660aed1)
      
     iii). Search in action:
           ![Image](https://github.com/user-attachments/assets/354cda99-92bd-40c8-9bc6-21f5f3a6170f)
   
      iv). Edit page with date picker & checkbox):
           ![Image](https://github.com/user-attachments/assets/b77f1857-a6c8-4b8e-ab22-4eed50ecb04e)
           ![Image](https://github.com/user-attachments/assets/5c3b2011-ebfc-4ca5-aafd-acf1bf154639)

      v). Sort dropdown:

   5. ### How to Run Locally
       
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





      What I Learned / Key Skills Demonstrated

      - Full-stack development with Flask & SQLAlchemy
      - CRUD operations, form handling, routing
      - Database schema updates & migration patterns
      - Dynamic queries: filtering (.filter), ordering (.order_by), null handling
      - Responsive UI with Bootstrap
      - Debugging common Flask/Jinja/SQLite issues (routing, templates, unbound variables)
        
     
     Future Improvements (Planned)

      - User authentication & multiple user support
      - Task categories/priority levels
      - Deployment to Render.com or Railway.app (live demo)
