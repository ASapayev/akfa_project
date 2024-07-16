from rest_framework import serializers
from aluminiy.models import AluProfilesData

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AluProfilesData
        fields = ['id', 'data']