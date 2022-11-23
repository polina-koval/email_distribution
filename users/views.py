from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from email_template.models import EmailTemplate
from django.contrib.auth import get_user_model
from users.tasks import send_email


User = get_user_model()


class SendingEmail(View):
    def get(self, request, pk):
        template_name = "test"
        emails = [User.objects.get(pk=pk).email]
        context = {"value_1": 'hello'}
        send_email.delay(
            template_name,
            context,
            emails=emails,
        )
        return redirect(reverse("admin:users_user_changelist"))
