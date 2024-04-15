from rest_framework import serializers
from .models import Norma



class NormaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Norma
        fields =['data']

