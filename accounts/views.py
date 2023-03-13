from django.shortcuts import render,redirect
from django.contrib import messages,auth

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
      return redirect('login')
  return render(request,'accounts/login.html')

def logout(request):
  auth.logout(request)
  messages.info(request,'you are logged out.')
  return redirect('login')