jttutor10@Mac module-1-django-basics-jtutor26 % cd projects/yet-another-pokedex
jttutor10@Mac yet-another-pokedex % python3 -m venv .venv
jttutor10@Mac yet-another-pokedex % source .venv/bin/activate
(.venv) jttutor10@Mac yet-another-pokedex % pip --install django

Usage:   
  pip <command> [options]

no such option: --install
(.venv) jttutor10@Mac yet-another-pokedex % pip install django
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
(.venv) jttutor10@Mac yet-another-pokedex % pip install --upgrade pip
Requirement already satisfied: pip in ./.venv/lib/python3.13/site-packages (25.1.1)
Collecting pip
  Using cached pip-25.2-py3-none-any.whl.metadata (4.7 kB)
Using cached pip-25.2-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.1.1
    Uninstalling pip-25.1.1:
      Successfully uninstalled pip-25.1.1
Successfully installed pip-25.2
(.venv) jttutor10@Mac yet-another-pokedex % django-admin startproject config .
(.venv) jttutor10@Mac yet-another-pokedex % python3 manage.py startapp yet-another-pokedex
CommandError: 'yet-another-pokedex' is not a valid app name. Please make sure the name is a valid identifier.
(.venv) jttutor10@Mac yet-another-pokedex % python3 manage.py startapp yet_another_pokedex
(.venv) jttutor10@Mac yet-another-pokedex % python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 21, 2025 - 20:10:19
Django version 5.2.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[21/Oct/2025 20:10:33] "GET / HTTP/1.1" 200 12068
(.venv) jttutor10@Mac yet-another-pokedex % python3 manage.py migrate
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
  (.venv) jttutor10@Mac yet-another-pokedex % python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 21, 2025 - 20:18:05
Django version 5.2.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[21/Oct/2025 20:18:12] "GET / HTTP/1.1" 200 12068
Not Found: /favicon.ico
[21/Oct/2025 20:18:13] "GET /favicon.ico HTTP/1.1" 404 2208
^C%