from unicodedata import name
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
# Add the following import
# from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')  

def index(request):
  return render(request, 'index.html')  

def teacherDashboard(request):
  return render(request, 'teacher-dashboard.html', { 'teachers': teachers })  

def studentDashboard(request):
  return render(request, 'student-dashboard.html', { 'students': students })   

def teacher_signup(request):
    # define tasks for handing POST request
    form = UserCreationForm()
    error_message = ''
    if request.method == 'POST':
        #capture form inputs from the usercreation form
        form = UserCreationForm(request.POST)
        #validate the form inputs
        if form.is_valid():
            #save the input values as a new user to the database
            user = form.save()
            #programmatically log the user in
            login(request, user)
            #redirect the user to the cats index page
            return redirect('index')
        # if form is invalid show error message
        else:
            error_message = 'Invalid credentials'
    # define tasks for handling GET request
    context = {'form': form, 'error_message': error_message}
    # redner a template with an empty form
    return render(request, 'registration/teacher_signup.html', context) 


def student_signup(request):
    # define tasks for handing POST request
    form = UserCreationForm()
    error_message = ''
    if request.method == 'POST':
        #capture form inputs from the usercreation form
        form = UserCreationForm(request.POST)
        #validate the form inputs
        if form.is_valid():
            #save the input values as a new user to the database
            user = form.save()
            #programmatically log the user in
            login(request, user)
            #redirect the user to the cats index page
            return redirect('index')
        # if form is invalid show error message
        else:
            error_message = 'Invalid credentials'
    # define tasks for handling GET request
    context = {'form': form, 'error_message': error_message}
    # redner a template with an empty form
    return render(request, 'registration/student_signup.html', context)     


class Teacher:
  def __init__(self, first_name, last_name, password, email, phone_num, sex, address, role, subject, description):
    self.first_name = first_name
    self.last_name = last_name
    self.password = password
    self.email = email
    self.phone_num = phone_num
    self.sex = sex
    self.address = address
    self.role = role
    self.subject = subject
    self.description = description


teachers = [
  Teacher('Jane', 'Rudo', 'password', 'j_r@yahoo.com', '123-456-7891', 'F', 'fake-address', 'Teacher', 'Math', 'Difficult'),
]  
print(teachers)
class Student:
  def __init__(self, first_name, last_name, password, email, phone_num, sex, address, role, grade, dob):
    self.first_name = first_name
    self.last_name = last_name
    self.password = password
    self.email = email
    self.phone_num = phone_num
    self.sex = sex
    self.address = address
    self.role = role
    self.grade = grade
    self.dob = dob


students = [
  Student('Jane', 'Rudo', 'password', 'j_r@yahoo.com', '123-456-7891', 'F', 'fake-address', 'Teacher', '10', '2000-02-22'),
]    