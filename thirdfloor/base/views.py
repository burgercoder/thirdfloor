from typing import Any

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return self.render_to_response({})
