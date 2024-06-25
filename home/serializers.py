from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class TechsunamiStringField(serializers.CharField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run_validation(self, data):

        if not isinstance(data, str):
            raise serializers.ValidationError("Data enter should be string type")

        data = data.upper()
        return super().run_validation(data)


class StudentSerializer(serializers.ModelSerializer):

    #customizable field
    name = TechsunamiStringField(max_length=100)

    class Meta:
        model = Student
        # field =['name','age']
        # exclude = ['id']
        fields = '__all__'

    def validate(self, data):

        if data['age']<18:
            raise serializers.ValidationError({'erros':"age cannot be less than 18"})

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'name cannot containe digits'})

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields ='__all__'
        # depth = 1  ? learn
