from typing import Callable, Optional, Type

from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.http.response import HttpResponseBase
from django.utils.deprecation import MiddlewareMixin


class SessionMiddleware(MiddlewareMixin):
    get_response: Callable[[WSGIRequest], HttpResponseBase] = ...
    SessionStore: Type[SessionStore] = ...

    def __init__(self, get_response: Optional[Callable] = ...) -> None: ...

    def process_request(self, request: HttpRequest) -> None: ...

    def process_response(
            self, request: WSGIRequest, response: HttpResponseBase
    ) -> HttpResponseBase: ...
