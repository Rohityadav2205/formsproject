from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import HttpResponse
from django.shortcuts import render


from .forms import StudentForm,BookForm
from .models import FormModel


# Create your views here.

# def index(request):
#     return HttpResponse("form page")


def form(request):
    d = {"student_name": "CR", "roll_number": "22334455", "mobile_number": "1122334455", "date_of_birth": "12/1/0000"}
    return render(request, 'form.html', {"form": StudentForm(initial=d)})


def bookform(request):
   if request.POST:
      newbook = Form(request.POST)
      if newbook.is_valid():
         newbook.save(commit=False)
         newbook.save()
         return HttpResponse("Book Saved")
   initial = {"bookname": "Recursion", "subject": "Recursion", "price": 100}
   return render(request, "book.html", {"form": BookForm(initial=initial)})


def Studentview(request):
    initial = {"name": "Popat", "rollno": "101"}
    return render(request, "student.html", {"form": StudentForm(initial=initial)})



def index(request):
    print(FormModel.objects.all())
    output = serializers.serialize("json", FormModel.objects.all())
    # return JsonResponse(output,safe=False)
    return HttpResponse(output, content_type="application/json")



def createUser(request):
    user = User.objects.create_user('sarthak', 'sarthak@gmail.com', 'sarthakpassword')
    user.save()
    return HttpResponse("Create")

def changepassword(request):
    user = User.objects.get(username='popat')
    user.set_password('newpassword')
    user.first_name = "Popat"
    user.last_name = "Lal"
    user.save()
    return HttpResponse("Password Changed")


def authenticateuser(request):
    user = authenticate(username='popat', password='newpassword')
    print(user)
    if user is not None:
        login(request, user)
        return HttpResponse(str(user))
    else:
        return HttpResponse("Login failed")


def dologout(request):
    logout(request)
    return HttpResponse("Logout")


def onlyloggedin(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return HttpResponse("Logged In" + str(request.user))
    return HttpResponse("Not Logged In")






