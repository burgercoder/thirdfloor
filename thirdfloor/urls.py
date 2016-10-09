from django.conf.urls import url  # type: ignore
from django.contrib import admin  # type: ignore

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
