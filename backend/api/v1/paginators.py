from rest_framework.pagination import PageNumberPagination


class LimitPageNumberPagination(PageNumberPagination):
    page_query_param = 'limit'
    page_size_query_param = 'page_size'
    page_size = 20
