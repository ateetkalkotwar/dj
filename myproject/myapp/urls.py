from django.urls import path
from . import views   # ✅ This imports your views.py

urlpatterns = [
    path('', views.student_form, name='student_form'),
    path('success/', views.success, name='success'),
]
