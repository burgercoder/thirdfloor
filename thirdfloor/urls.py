from django.conf.urls import url
from django.contrib import admin

# pylint: disable=invalid-name
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
