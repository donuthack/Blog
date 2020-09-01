from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MiniPublicationSerializer, CreateOrUpdateSerializer, PublicationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import permissions, filters
from .models import Publication
from .filter import PublicationFilter, PaginationBlog
from django.utils import timezone


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = PublicationFilter
    search_fields = ['title']
    ordering_fields = ['publication_date']
    pagination_class = PaginationBlog


    def get_serializer_class(self):
        if self.action == 'update' or self.request == 'create':
            return CreateOrUpdateSerializer
        elif self.action == 'retrieve':
            return PublicationSerializer
        else:
            return MiniPublicationSerializer
