from email_distribution.celery_app import app
from email_template.models import EmailTemplate


@app.task()
def send_email(*args, **kwargs):
    return EmailTemplate.send(*args, **kwargs)
