from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from apps.policeman.models import Policeman
from django.contrib.auth.password_validation import validate_password
from apps.policeman.validators import validate_only_numerical


class PolicemanCreateSerializer(serializers.ModelSerializer):
    identification_number = serializers.CharField(validators=[
        validate_only_numerical,
        UniqueValidator(queryset=Policeman.objects.all())
    ])
    password = serializers.CharField(validators=[validate_password])
    confirm_password = serializers.CharField()

    class Meta:
        model = Policeman
        fields = ['identification_number', 'name', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise ValidationError(
                "The password and confirm_password fields must match",
                code='passwords_not_match',
            )
        return attrs

    def create(self, validated_data):
        return Policeman.objects.create_user(
            identification_number=validated_data.get('identification_number'),
            password=validated_data.get('password'),
            name=validated_data.get('name')
        )


class PolicemanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policeman
        fields = ['name']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class PolicemanUpdatePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[validate_password])
    confirm_password = serializers.CharField()

    class Meta:
        model = Policeman
        fields = ['password', 'confirm_password']

    def validate(self, attrs):
        if ('password' not in attrs) and ('confirm_password' not in attrs):
            return attrs

        if ('password' not in attrs) and ('confirm_password' in attrs):
            raise ValidationError(
                "password field must not be null",
                code='passwords_not_match',
            )

        if ('confirm_password' not in attrs) and ('password' in attrs):
            raise ValidationError(
                "confirm_password field must not be null",
                code='passwords_not_match',
            )

        if attrs.get('password') != attrs.get('confirm_password'):
            raise ValidationError(
                "The password and confirm_password fields must match",
                code='passwords_not_match',
            )
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class PolicemanReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policeman
        fields = ['id','identification_number','name']
