from rest_framework import serializers
from apps.policeman.models import Policeman


class PolicemanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policeman
        fields = '__all__'
