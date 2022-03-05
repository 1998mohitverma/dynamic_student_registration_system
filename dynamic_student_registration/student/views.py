from django.shortcuts import render, redirect
from django.views import View
from .forms import Student_form
from student.forms import Student_form
from .models import Student_Table
# Create your views here.

class add_student(View):
    def get(self, request):
        return render(request, 'student/student.html')

    def post(self, request):
        name = request.POST['name']
        course = request.POST['course']
        number = request.POST['number']
        email = request.POST['email']
        student = Student_Table(name=name,course=course,number=number,email=email)
        student.save()
        msg = 'Your details has been registered'
        context = {'msg':msg}
        return render(request, 'student/student.html',context)

class get_students(View):
    def get(self,request):
        stu = Student_Table.objects.all()
        context = {'stu':stu}
        return render(request, 'student/get_student.html',context)

class update_student(View):
    def get(self,request,id):
        pi = Student_Table.objects.get(pk=id)
        fm = Student_form(instance=pi)
        context = {'form':fm}
        return render(request, 'student/update.html',context)

    def post(self,request,id):
        pi = Student_Table.objects.get(pk=id)
        fm = Student_form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('get_student')

class delete_record(View):
    def post(self,request,id):
        pi = Student_Table.objects.get(pk=id)
        pi.delete()
        return redirect('get_student')

class about_page(View):
    def get(self, request):
        return render(request, 'student/about.html')

def add_multiple(request):
    return render(request, 'student/add_multiple.html')

def delete_multiple(request):
    return render(request, 'student/delete_multiple.html')