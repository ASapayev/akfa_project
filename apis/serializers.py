from rest_framework import serializers
from aluminiy.models import AluProfilesData,LengthOfProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AluProfilesData
        fields = ['id', 'data']

class LengthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LengthOfProfile
        fields = ['id', 'artikul','length','ves_za_shtuk','ves_za_metr']