from rest_framework.pagination import PageNumberPagination


class StandardPageNumberPagination(PageNumberPagination):
    page_size              = 6
    max_page_size          = 1000
    page_query_param       = 'page_number'
    page_size_query_param  = 'per_page'

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        response.data['page_number'] = self.page.number
        return response
