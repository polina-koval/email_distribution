from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    from users.views import SendingEmail
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser", "email_test"]

    def get_urls(self):
        urls = super(UserAdmin, self).get_urls()
        urls += [
            url(
                r"^send-email/(?P<pk>\d+)$",
                self.SendingEmail.as_view(),
                name="send-email",
            ),
        ]
        return urls

    def email_test(self, obj):
        return format_html(
            '<a class="button" href="{}">Send</a>',
            reverse("admin:send-email", args=[obj.pk]),
        )

    email_test.short_description = "Email"
