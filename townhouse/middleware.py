import re

from django.http import JsonResponse
from core.urls import *

class SQLSecurityMiddleware:
    """validate for sql-injection characters"""
    pure_sql_view = [f'/table/{u.name}/' for u in urlpatterns] + [f'/table/{i[0]}/' for i in router.registry]

    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        if request.path in self.pure_sql_view:
            error = self.validate(dict(request.GET))
            if error:
                return JsonResponse({'errors': error}, status=400)
        response = self._get_response(request)
        return response

    def validate(self, data):
        error = []
        for field, value in data.items():
            if isinstance(value, str) and re.search(r"[\"'=();]+", value):
                error.append(f"Argument '{field}' should not contain special characters")
            if isinstance(value, list):
                for v in value:
                    if re.search(r"[\"'=();]+", v):
                        error.append(f"Argument '{field}' should not contain special characters")
        return error
