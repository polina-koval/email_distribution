import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTING_MODULE", "email_distribution.settings")
app = Celery("email_distribution")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

