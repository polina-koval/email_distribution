import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTING_MODULE", "email_distribution.settings")
app = Celery("email_distribution")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-email-every-5-minute': {
        'task': 'users.tasks.delayed_send_email',
        'schedule': crontab(minute='*/5')
    }
}
