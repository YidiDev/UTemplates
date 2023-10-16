from django.http import HttpResponse
from ..rendering import render


def render_to_response(response_content: any, **kwargs) -> HttpResponse:
    response_content: str = render(response_content)
    return HttpResponse(response_content, **kwargs)
