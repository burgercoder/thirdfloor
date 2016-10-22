from django.conf.urls import url
from django.contrib import admin

from thirdfloor.base.views import IndexView

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^admin/', admin.site.urls),
    url(r'^.*/$', IndexView.as_view(), name='index'),
]
