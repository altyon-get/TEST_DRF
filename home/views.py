from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({'status': 200, 'payload': serializer.data})

# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)
#     return Response({'status': 200,'payload': serializer.data})
#
# @api_view(['POST'])
# def post_student(request):
#     data=request.data
#     serializer = StudentSerializer(data=request.data)
#
#     if not serializer.is_valid():
#         return Response({'status': 403,'errors':serializer.errors, 'message': 'something went wrong'})
#
#     serializer.save()
#
#     return Response({'status': 200, 'payload': serializer.data , 'message':'data uploaded'})
#
# @api_view(['PATCH'])
# def update_student(request, student_id):
#     print(student_id)
#     try:
#         student_obj = Student.objects.get(id=student_id)
#         # print(student_obj.name)
#         # print(student_obj.age)
#         # data = request.data
#         serializer = StudentSerializer(student_obj, data=request.data, parital=True)
#         if not serializer.is_valid():
#             return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
#         serializer.save()
#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalid id'})
#
# @api_view(['DELETE'])
# def delete_student(request, student_id):
#     try:
#         student_obj = Student.objects.get(id=student_id)
#         student_obj.delete()
#         return Response({'status': 500, 'message': 'Entry deleted'})
#     except Exception as e:
#         return Response({'Status': 403, 'message': 'invalid id'})


class StudentAPI(APIView):

    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({'status': 200, 'payload': serializer.data})


    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})

        serializer.save()

        return Response({'status': 200, 'payload': serializer.data, 'message': 'data uploaded'})

    def put(self,request):
        student_id = request.data['id']
        try:
            student_obj = Student.objects.get(id=student_id)
            # print(student_obj.name)
            # print(student_obj.age)
            # data = request.data
            serializer = StudentSerializer(student_obj, data=request.data)
            if not serializer.is_valid():
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
            serializer.save()
            return Response({'message': 'success'})
        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id'})

    def patch(self, request):
        student_id = request.data['id']
        print(student_id)
        try:
            student_obj = Student.objects.get(id=student_id)
            print(student_obj)
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
            serializer.save()
            return Response({'message': 'success'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'invalid id'})

    def delete(self, request):
        student_id = request.data['id']
        try:
            student_obj = Student.objects.get(id=student_id)
            student_obj.delete()
            return Response({'status': 500, 'message': 'Entry deleted'})
        except Exception as e:
            return Response({'Status': 403, 'message': 'invalid id'})
