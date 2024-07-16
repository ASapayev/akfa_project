
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from aluminiy.models import AluProfilesData
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 50  # Number of items per page
    page_size_query_param = 'page_size'  # Override default page size query parameter name
    max_page_size = 1000 


class ProfileViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = AluProfilesData.objects.all().order_by('created_at')
    serializer_class = ProfileSerializer
    pagination_class = CustomPagination



    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)