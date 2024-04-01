from django.shortcuts import render , redirect
from .models import student,course
from django import forms
# Create your views here.

class Studentform(forms.ModelForm):
   class Meta:
        model = student
        fields = ['name', 'password', 'email', 'courses']

class Courseform(forms.ModelForm):
    class Meta:
        model = course
        fields = ['course.name']




def students(request):
    students_list = student.objects.all()
    form = Studentform()
    if request.method == 'POST':
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request, 'app/students.html', {'students_list': students_list, 'form': form})

def courses(request):
    courses_list = course.objects.all()
    form = Courseform()
    if request.method == 'POST':
        form = Courseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("courses")
    return render(request, 'app/courses.html', {'courses_list': courses_list, 'form': form})

def details(request, studentID):
    student = student.objects.get(id=studentID)
    available_courses = course.objects.exclude(student=student)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        if course_id:
            course = course.object.get(id=course_id)
            student.courses.add(course)
            return redirect('details', studentID)
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})    




    

