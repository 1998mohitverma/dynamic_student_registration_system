"""dynamic_student_registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import View
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_student.as_view(),name='student'),
    path('get_student', views.get_students.as_view(),name='get_student'),
    path('update_student/<int:id>/', views.update_student.as_view(),name='update_student'),
    path('delete_record/<int:id>/', views.delete_record.as_view(),name='delete_record'),
    path('about/', views.about_page.as_view(),name='about'),
    path('add_mul/', views.add_multiple,name='add_multiple'),
    path('delete_mul/', views.delete_multiple,name='delete_multiple'),
]