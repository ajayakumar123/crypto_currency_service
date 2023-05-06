Python: 3.8.x (64 bit)
Framework: Django 3.x

Clone Repository:
$ git clone https://bitbucket.org/simplifyworkforce/svms-configurator-service.git

Create & Activate Virtualenv:
$ cd <app_root>
$ python3 -m venv venv
$ venv/scripts/activate 

Install Dependencies:
(venv) $ pip install -r requirements.txt

Run DB migrations:
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate

Start Server:
(venv) $ python manage.py runserver 0.0.0.0:8000

create superuser:
(venv) $ python manage.py createsuperuser
username:hradmin
Email adress: hradmin@gmail.com
password:demo@123
