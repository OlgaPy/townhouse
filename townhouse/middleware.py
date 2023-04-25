import re
from typing import Dict
import json
from django.http import JsonResponse
from core.urls import *


class SQLSecurityMiddleware:
    """validate for sql-injection characters"""

    def __init__(self, get_response):
        self._get_response = get_response

        self.exclude = 'documents'
        self.pure_sql_view = [f'/table/{u.name}/' for u in urlpatterns
                              if u.name not in self.exclude] + \
                             [f'/table/{i[0]}/' for i in router.registry
                              if i[0] not in self.exclude]

    def __call__(self, request):
        if request.path in self.pure_sql_view:
            params = dict(request.GET) if request.method == 'GET' else {}
            params.update(dict(json.loads(request.body)) if getattr(request, 'body', '') else {})
            error = self.validate(params)
            if error:
                return JsonResponse({'errors': error}, status=400)
        response = self._get_response(request)
        return response

    @staticmethod
    def validate(data: Dict):
        error = []
        for field, value in data.items():
            if isinstance(value, str) and re.search(r"[\"'=();]+", value):
                error.append(f"Argument '{field}' should not contain special characters")
            if isinstance(value, list):
                for v in value:
                    if re.search(r"[\"'=();]+", v):
                        error.append(f"Argument '{field}' should not contain special characters")
        return error
