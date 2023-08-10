from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    current_orders = Order.objects.filter(current_worker=user)
    context ={
        'orders':current_orders
    }
    return render(request,'dashboard/workers.html',context)