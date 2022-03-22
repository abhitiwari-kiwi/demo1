from django.shortcuts import render, redirect
from django.views import View


from .forms import studentinformationform
from .models import studentinformation


class Home(View):
    def get(self, request):
        students = studentinformation.objects.all()
        context = {'student': students}
        return render(request, 'student/home.html', context)

# Function for adding new students
def add(request):
    # Accessing the form to add details of a students
    form=studentinformationform()
    if request.method=='POST':
        form=studentinformationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=studentinformationform()
    context={'form': form}
    return render(request, 'student/add.html', context)

# Function for editing an existing student informartion
def edit(request, pk):
    # Get the details of that particular student
    students=studentinformation.objects.get(id=pk)
    form=studentinformationform(instance=students)
    if request.method=='POST':
        form=studentinformationform(request.POST, instance=students)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form': form}
    return render(request, 'student/edit.html', context)

# Function to delete a particular student details 
def delete(request, pk):
    # Get the details of that particular student
    students=studentinformation.objects.get(id=pk)
    if request.method=='DELETE':
        students.delete()
        return redirect('home')
    context={'student': students}
    return render(request, 'student/delete.html', context)