from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps.person.models import Person


class PersonSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[
        UniqueValidator(queryset=Person.objects.all())
    ])
    class Meta:
        model = Person
        fields = '__all__'

class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name']
