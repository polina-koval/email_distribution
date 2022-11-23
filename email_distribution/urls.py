from django.conf.urls import url
from django.contrib import admin

from users.views import PixelView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^p/(?P<pk>\w+).gif$', PixelView.as_view(), name='email_pixel'),
]
