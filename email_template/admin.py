from django.contrib import admin

from email_template.models import EmailTemplate


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ["template_key", "subject", "from_email", "to_email"]

