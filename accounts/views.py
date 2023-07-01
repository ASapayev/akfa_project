from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .models import User


# Create your views here.
def login(request):
  if request.user.is_authenticated:
    return redirect('home')
  elif request.method =='POST':
    email =request.POST.get('email',None)
    password =request.POST.get('password',None)
    user = auth.authenticate(email=email,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('home')
    else:
      messages.info(request,'Password or e-mail incorrect!')
      return redirect('login')
  return render(request,'accounts/login.html')

def logout(request):
  auth.logout(request)
  messages.info(request,'you are logged out.')
  return redirect('login')

def registerUser(request):
  if request.method =='POST':
    username = request.POST.get('username')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User()
    user.first_name = firstname
    user.last_name = lastname
    user.username = username
    user.email =email
    user.set_password(password)
    user.save()
    return redirect('login')
  else:
    return render(request,'accounts/register.html')