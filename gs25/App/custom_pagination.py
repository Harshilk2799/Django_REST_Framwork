from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "custom_page"
    page_size_query_param = "records"
    max_page_size = 4
    last_page_strings = ("end",)



class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2   
    # limit_query_param = "l"
    # offset_query_param = "of"
    max_limit = 5


class CustomCursorPagination(CursorPagination):
    page_size = 3 
    ordering = ["-roll"]
    cursor_query_param = "cur"