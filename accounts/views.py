from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .models import User,UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm,AccountForm


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
  
@login_required(login_url='/accounts/login/')
def myAccount(request):
  user = request.user
  user_profile =  UserProfile.objects.get(user = user)
  
  if request.method =='POST':
    user_form = AccountForm(request.POST, instance= user)
    user_profile_form =UserProfileForm(request.POST,request.FILES,instance= user_profile,)
    if user_form.is_valid() and user_profile_form.is_valid():
      user_form.save()
      user_profile_form.save()
      return redirect('myAccount')
  else:
    user_form = AccountForm(instance=user)
    user_profile_form =UserProfileForm(instance= user_profile)
    context ={
      'user':user,
      'user_profile_2':user_profile,
      'user_form':user_form,
      'user_profile_form':user_profile_form
    }
    return render(request,'accounts/my_profile.html',context)