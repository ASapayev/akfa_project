from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Order
from django.contrib.auth.decorators import login_required
import ast
from accounts.models import User
from django.core.paginator import Paginator



@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    if user.role == 2:
        current_orders = Order.objects.filter(work_type__gte = 6).order_by('-created_at')

    else:
        current_orders = Order.objects.all().order_by('-created_at')


    paginator = Paginator(current_orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)


    context ={
        'orders':page_obj
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


@login_required(login_url='/accounts/login/')
def order_delete(request,id):
    order = Order.objects.get(id = id)
    order.delete()
    return redirect('order')


@login_required(login_url='/accounts/login/')
def status_change_to_done(request,id):
    order = Order.objects.get(id = id)
    order.work_type =10
    order.save()
    return redirect('order')


