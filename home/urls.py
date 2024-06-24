from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    # path('', home),
    # path('student/', post_student),
    # path('update_student/<student_id>/', update_student),
    # path('delete_student/<student_id>/', delete_student),
    path('student/', StudentAPI.as_view()),
    path('get_book/', get_book)
]