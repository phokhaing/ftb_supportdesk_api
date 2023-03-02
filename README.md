# DJANGO CONFIGURATION

------------------------------------
DOCUMENT TO SETUP PROJECT:
------------------------------------

Noted: 
   - python manage.py inspectdb > models.py : Auto generate Models from existing Database and table
   - python manage.py dbshell : for test db connection
   - python manage.py migrate --fake-initial : skips the migrations where the tables are already exist

I. Setup environment:
   - pip3 install virtualenv: install virtualenv via cmd administrator
   - virtualenv venv: clone new venv

II. Install Django:
   - pip install django djangorestframework django-filter

III. work with requirements.txt:
   - pip freeze : list all modules installed
   - pip freeze > requirements.txt : copy all modules installed into file requirements.txt
   - pip install -r requirements.txt : install all modules from requirements.txt

IV. Start project:
   - django-admin startproject project_name . :create project_name in current directory

V. Start app:
   - python manage.py startapp appraisal: create new app name appraisal
   - python manage.py startapp purchase: create new app name purchase
   - python manage.py startapp loan: create new app name purchase

V. Configure setting.py:
   - add new line inside:
      INSTALL_APPS = [
         'rest_framework',
         'appraisal',
         'purchase',
         'loan'
      ]