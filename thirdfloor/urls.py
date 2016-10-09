from django.conf.urls import url  # type: ignore
from django.contrib import admin  # type: ignore

# pylint: disable=invalid-name
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
