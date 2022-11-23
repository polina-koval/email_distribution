import urlparse
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.views.generic import View

from email_template.models import EmailTemplate
from users.models import Email
from users.tasks import send_email

User = get_user_model()


class SendingEmail(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        template_name = "test"
        template = EmailTemplate.objects.get(template_key=template_name)
        emails = [user.email]
        context = {"value_1": 'hello'}
        email = Email.objects.create(
            user=user,
            template=template,
        )
        url1 = request.build_absolute_uri("/")[:-1]
        url2 = reverse("email_pixel", kwargs={"pk": email.pk})
        url = urlparse.urljoin(url1, url2)
        send_email.delay(template_name, context, emails=emails, url=url)

        return redirect(reverse("admin:users_user_changelist"))


class PixelView(View):
    @cache_control(must_revalidate=True, max_age=60)
    def get(self, request, pk):
        pixel_image = b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b"  # pylint:disable=line-too-long
        email = Email.objects.get(pk=pk)
        email.is_open = True
        email.save()
        return HttpResponse(pixel_image, content_type="image/gif")
