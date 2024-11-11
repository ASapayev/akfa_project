from rest_framework import serializers
from aluminiy.models import AluProfilesData,LengthOfProfile,Mastergroup,BuxgalterNazvaniye,RazlovkaTermo,RazlovkaObichniy

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AluProfilesData
        fields = ['id', 'data']

class RazlovkaTermo1101Serializer(serializers.ModelSerializer):
    class Meta:
        model = RazlovkaTermo
        fields = ['id','parent_id','zsap_code','zkratkiy','psap_code','pkratkiy','ssap_code','skratkiy','nsap_code','nkratkiy','ksap_code','kratkiy','sap_code7','kratkiy7']

class RazlovkaTermo1201Serializer(serializers.ModelSerializer):
    class Meta:
        model = RazlovkaTermo
        fields = ['id','parent_id','esap_code','ekratkiy','zsap_code','zkratkiy','psap_code','pkratkiy','ssap_code','skratkiy','asap_code','akratkiy','nsap_code','nkratkiy','ksap_code','kratkiy','sap_code7','kratkiy7','fsap_code','fkratkiy','sap_code75','kratkiy75']

class Razlovka1101Serializer(serializers.ModelSerializer):
    class Meta:
        model = RazlovkaObichniy
        fields = ['id', 'esap_code','ekratkiy','zsap_code','zkratkiy','psap_code','pkratkiy','ssap_code','skratkiy','sap_code7','kratkiy7']

class Razlovka1201Serializer(serializers.ModelSerializer):
    class Meta:
        model = RazlovkaObichniy
        fields = ['id', 'esap_code','ekratkiy','zsap_code','zkratkiy','psap_code','pkratkiy','ssap_code','skratkiy','asap_code','akratkiy','nsap_code','nkratkiy','sap_code7','kratkiy7','fsap_code','fkratkiy','sap_code75','kratkiy75']

class LengthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LengthOfProfile
        fields = ['id', 'artikul','component','ves_za_metr']

class MasterGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mastergroup
        fields = ['id', 'sep','pokritiya','combination','new_group','sena_usd']

class BuxgalterNazvaniyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuxgalterNazvaniye
        fields = ['id', 'colected','combination','surface_treatment','zavod_aluminiy','zavod_aluminiy_benkam']