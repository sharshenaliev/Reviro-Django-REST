from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from geopy.geocoders import Nominatim
from drf_spectacular.utils import extend_schema_field
from backend.models import Product, Establishment


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "The passwords don't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['email'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    key = serializers.CharField(read_only=True)

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        user = authenticate(username=validated_data['email'],
                            password=validated_data['password'])
        if not user:
            raise exceptions.AuthenticationFailed('Email or password entered incorrectly.')
        token, created = Token.objects.get_or_create(user=user)
        return token


class ProductSerializer(serializers.ModelSerializer):

     class Meta:
        model = Product
        fields = '__all__'


class EstablishmentSerializer(serializers.ModelSerializer):
    opening_hours = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = Establishment
        fields = '__all__'

    def validate(self, attrs):
        address = f"Бишкек, {attrs['location']}"
        geolocator = Nominatim(user_agent="myApp")
        location = geolocator.geocode(address)
        if not location:
            raise serializers.ValidationError({"location": "The address is not valid."})
        return attrs

    @extend_schema_field({'type': 'string', })
    def get_opening_hours(self, instance):
        return f'{instance.opening_hour.strftime("%H:%M")} - {instance.closing_hour.strftime("%H:%M")}'
