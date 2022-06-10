from rest_framework import serializers
from modules.maaji.models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']

class Cliente_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class Producto_serializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class Tienda_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'

class Factura_serializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
