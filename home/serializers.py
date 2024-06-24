from rest_framework import serializers
from .models import *



# class TechsunamiStringField()

class StudentSerializer(serializers.ModelSerializer):
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
