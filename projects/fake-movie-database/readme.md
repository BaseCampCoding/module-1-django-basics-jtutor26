jttutor10@Mac module-1-django-basics-jtutor26 % cd projects/fake-movie-database
jttutor10@Mac fake-movie-database % python3 -m venv .venv
jttutor10@Mac fake-movie-database % source .venv/bin/activate
(.venv) jttutor10@Mac fake-movie-database % pip install django
Collecting django
  Using cached django-5.2.7-py3-none-any.whl.metadata (4.1 kB)
Collecting asgiref>=3.8.1 (from django)
  Using cached asgiref-3.10.0-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from django)
  Using cached sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Using cached django-5.2.7-py3-none-any.whl (8.3 MB)
Using cached asgiref-3.10.0-py3-none-any.whl (24 kB)
Using cached sqlparse-0.5.3-py3-none-any.whl (44 kB)
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.10.0 django-5.2.7 sqlparse-0.5.3

[notice] A new release of pip is available: 25.1.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
(.venv) jttutor10@Mac fake-movie-database % django-admin startproject config
(.venv) jttutor10@Mac fake-movie-database % python3 manage.py startapp fake_movie_database
/Library/Frameworks/Python.framework/Versions/3.13/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/jttutor10/bcca-assignments/Unit 5 DJango/module-1-django-basics-jtutor26/projects/fake-movie-database/manage.py': [Errno 2] No such file or directory
(.venv) jttutor10@Mac fake-movie-database % django-admin startproject config .
(.venv) jttutor10@Mac fake-movie-database % python3 manage.py startapp fake_movie_database
(.venv) jttutor10@Mac fake-movie-database % python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(.venv) jttutor10@Mac fake-movie-database % python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 22, 2025 - 13:50:01
Django version 5.2.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[22/Oct/2025 13:50:04] "GET / HTTP/1.1" 200 12068
Not Found: /favicon.ico
[22/Oct/2025 13:50:05] "GET /favicon.ico HTTP/1.1" 404 2208