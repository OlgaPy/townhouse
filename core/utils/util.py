from rest_framework import pagination


class DefaultViewSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'limit'
