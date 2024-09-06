from rest_framework import serializers
from aluminiy.models import AluProfilesData,LengthOfProfile,Mastergroup,BuxgalterNazvaniye

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AluProfilesData
        fields = ['id', 'data']

class LengthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LengthOfProfile
        fields = ['id', 'artikul','length','ves_za_shtuk','ves_za_metr']

class MasterGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mastergroup
        fields = ['id', 'sep','pokritiya','combination','new_group','sena_usd']

class BuxgalterNazvaniyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuxgalterNazvaniye
        fields = ['id', 'colected','combination','surface_treatment','zavod_aluminiy','zavod_aluminiy_benkam']