from django.contrib import admin
from .models import Student_Table
# Register your models here.
@admin.register(Student_Table)
class Student_admin(admin.ModelAdmin):
    list_display = ['id','name','course','number','email']