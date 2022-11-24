# Email distribution project  
The project allows you to send emails by storing templates in the database. The opening of the email is also tracked by a pixel built into the email. Celery and Redis are used.

## Getting Started  
The first thing to do is to clone the repository:  

```sh
$ git clone https://github.com/polina-koval/email_distribution.git
$ cd email_distribution
```  

Create a virtual environment to install dependencies in and activate it:  

```sh
$ virtualenv venv  
$ source venv/bin/activate
```

Then install the dependencies:  

```sh
(venv)$ pip install -r requirements.txt
```  

There is a file in the repo ".env.example", this file for use in local development. 
Duplicate this file as .env in the root of the project and update the environment 
variables SECRET_KEY, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, etc.  

```sh
$ cp .env.example .env
```

Once pip has finished downloading the dependencies and the variable is updated:  
 
Django:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
(venv)$ python manage.py runserver
```  

Redis:
```sh
(venv)$ docker run -d -p 6379:6379 redis
```  

Celery:
```sh
(venv)$ celery -A email_distribution worker -l info 
```

After configuring and running, go to the admin panel. 
In it(users app), as a test, you can send emails to existing users
(just create email template with template_key = "test"). In template you can
use value in format {{value}}. Value can be user.username, user.email, 
user.first_name, user.last_name, etc.
