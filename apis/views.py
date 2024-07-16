
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from aluminiy.models import AluProfilesData


class ProfileViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    
    def list(self, request):
        queryset = AluProfilesData.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)