from email_distribution.celery_app import app
from email_template.models import EmailTemplate
from users.models import User


@app.task()
def send_email(*args, **kwargs):
    EmailTemplate.send(*args, **kwargs)


@app.task()
def delayed_send_email():
    for user in User.objects.all():
        template_name = "test"
        emails = [user.email]
        context = {"value_1": 'hello'}
        EmailTemplate.send(
            template_name,
            context,
            emails=emails,
        )
