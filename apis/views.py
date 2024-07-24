
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer,LengthProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from aluminiy.models import AluProfilesData,LengthOfProfile


class ProfileViewSet(viewsets.ViewSet):
   
    
    def list(self, request):
        queryset = AluProfilesData.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)


class LengthProfileViewSet(viewsets.ViewSet):
   
    
    def list(self,request):
        queryset = LengthOfProfile.objects.all()
        serializer = LengthProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)