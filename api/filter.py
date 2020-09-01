from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from .models import Publication
from rest_framework.response import Response


class PublicationFilter(filters.FilterSet):
    pub_date = filters.DateFromToRangeFilter(field_name="publication_date")

    class Meta:
        model = Publication
        fields = ['author', 'pub_date']


class PaginationBlog(PageNumberPagination):
    page_size = 3
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
