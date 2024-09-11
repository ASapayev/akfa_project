
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer,LengthProfileSerializer,MasterGroupSerializer,BuxgalterNazvaniyeSerializer,Razlovka1101Serializer,Razlovka1201Serializer,RazlovkaTermo1101Serializer,RazlovkaTermo1201Serializer
from rest_framework import viewsets
from rest_framework.response import Response
from aluminiy.models import AluProfilesData,LengthOfProfile,BuxgalterNazvaniye,Mastergroup,RazlovkaObichniy,RazlovkaTermo


class ProfileViewSet(viewsets.ViewSet):
   
    
    def list(self, request):
        queryset = AluProfilesData.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    
class RazlovkaAluSimple1101ViewSet(viewsets.ViewSet):
   
    
    def list(self, request):
        queryset = RazlovkaObichniy.objects.all()
        serializer = Razlovka1101Serializer(queryset, many=True)
        return Response(serializer.data)
    
class RazlovkaAluTermo1101ViewSet(viewsets.ViewSet):
   
    
    def list(self, request):
        queryset = RazlovkaTermo.objects.all()
        serializer = RazlovkaTermo1101Serializer(queryset, many=True)
        return Response(serializer.data)
    
class RazlovkaAluTermo1201ViewSet(viewsets.ViewSet):
   
    
    def list(self, request):
        queryset = RazlovkaTermo.objects.all()
        serializer = RazlovkaTermo1201Serializer(queryset, many=True)
        return Response(serializer.data)
    
class RazlovkaAluSimple1201ViewSet(viewsets.ViewSet):
   
    
    def list(self, request):
        queryset = RazlovkaObichniy.objects.all()
        serializer = Razlovka1201Serializer(queryset, many=True)
        return Response(serializer.data)





class LengthProfileViewSet(viewsets.ViewSet):
   
    
    def list(self,request):
        queryset = LengthOfProfile.objects.all()
        serializer = LengthProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    
class MasterGroupViewSet(viewsets.ViewSet):
   
    
    def list(self,request):
        queryset = Mastergroup.objects.all()
        serializer = MasterGroupSerializer(queryset, many=True)
        return Response(serializer.data)
    
class BuxgalterNazvaniyeViewSet(viewsets.ViewSet):
   
    
    def list(self,request):
        queryset = BuxgalterNazvaniye.objects.all()
        serializer = BuxgalterNazvaniyeSerializer(queryset, many=True)
        return Response(serializer.data)

