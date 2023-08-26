from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from django.contrib.auth.decorators import login_required
import ast
from accounts.models import User



@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    if user.role == 2:
        current_orders = Order.objects.filter(work_type__gte = 6).order_by('-created_at')

    else:
        current_orders = Order.objects.all().order_by('-created_at')

    context ={
        'orders':current_orders
    }
    return render(request,'dashboard/workers.html',context)


@login_required(login_url='/accounts/login/')
def order_detail(request,id):
    order = Order.objects.get(id = id)
    
    context ={
        'order':order
    }
    paths =  order.paths
    
    if order.work_type == 5:
        workers = User.objects.filter(role = 1)
        context['workers'] =workers

    for key,val in paths.items():
        context[key] = val
    return render(request,'order/order_detail.html',context)