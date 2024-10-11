from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Order,OrderPVX
from django.contrib.auth.decorators import login_required
import ast
from radiator.models import OrderRadiator
from accounts.models import User
from django.core.paginator import Paginator
from accounts.decorators import allowed_users
from accessuar.models import OrderACS,OrderAKP,OrderProchiye
from kraska.models import OrderKraska


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def index(request):
    user = request.user
    if user.role == 'user1':
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
@allowed_users(allowed_roles=['admin','moderator'])
def index_akp(request):
    current_orders = OrderAKP.objects.all().order_by('-created_at')

    paginator = Paginator(current_orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)


    context ={
        'orders':page_obj
    }
    return render(request,'dashboard/workers_akp.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def index_prochiye(request):
    current_orders = OrderProchiye.objects.all().order_by('-created_at')

    paginator = Paginator(current_orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)


    context ={
        'orders':page_obj
    }
    return render(request,'dashboard/workers_prochiye.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def index_radiator(request):
    current_orders = OrderRadiator.objects.all().order_by('-created_at')

    paginator = Paginator(current_orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)


    context ={
        'orders':page_obj
    }
    return render(request,'dashboard/workers_radiator.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def index_accessuar(request):
    current_orders = OrderACS.objects.all().order_by('-created_at')

    paginator = Paginator(current_orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)


    context ={
        'orders':page_obj
    }
    return render(request,'dashboard/workers_accessuar.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def index_pvc(request):
    current_orders = OrderPVX.objects.all().order_by('-created_at')


    paginator = Paginator(current_orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)


    context ={
        'orders':page_obj
    }
    return render(request,'dashboard/workers_pvc.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def order_detail(request,id):
    order = Order.objects.get(id = id)
    
    context ={
        'order':order
    }
    paths =  order.paths
    
    if order.work_type == 5:
        workers = User.objects.filter(role = 'moderator')
        context['workers'] =workers

    for key,val in paths.items():
        context[key] = val
    return render(request,'order/order_detail.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_detail_pvc(request,id):
    order = OrderPVX.objects.get(id = id)
    
    context ={
        'order':order
    }
    paths =  order.paths
    
    if order.work_type == 5:
        workers = User.objects.filter(role =  'moderator')
        context['workers'] =workers

    for key,val in paths.items():
        context[key] = val
    return render(request,'order/order_detail_pvc.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_detail_radiator(request,id):
    order = OrderRadiator.objects.get(id = id)
    
    context ={
        'order':order
    }
    paths =  order.paths
    
    if order.work_type == 5:
        workers = User.objects.filter(role =  'moderator')
        context['workers'] =workers

    for key,val in paths.items():
        context[key] = val
    return render(request,'order/order_detail_radiator.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_detail_akp(request,id):
    order = OrderAKP.objects.get(id = id)
    
    context ={
        'order':order
    }
    paths =  order.paths
    
    if order.work_type == 5:
        workers = User.objects.filter(role =  'moderator')
        context['workers'] =workers

    for key,val in paths.items():
        context[key] = val
    return render(request,'order/order_detail_akp.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_detail_prochiye(request,id):
    order = OrderProchiye.objects.get(id = id)
    
    context ={
        'order':order
    }
    paths =  order.paths
    
    if order.work_type == 5:
        workers = User.objects.filter(role =  'moderator')
        context['workers'] =workers

    for key,val in paths.items():
        context[key] = val
    return render(request,'order/order_detail_prochiye.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_detail_kraska(request,id):
    order = OrderKraska.objects.get(id = id)
    
    context ={
        'order':order
    }
    paths =  order.paths
    
    if order.work_type == 5:
        workers = User.objects.filter(role =  'moderator')
        context['workers'] =workers

    for key,val in paths.items():
        context[key] = val
    return render(request,'order/order_detail_kraska.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_detail_accessuar(request,id):
    order = OrderACS.objects.get(id = id)
    
    context ={
        'order':order
    }
    paths =  order.paths
    
    if order.work_type == 5:
        workers = User.objects.filter(role =  'moderator')
        context['workers'] =workers

    for key,val in paths.items():
        context[key] = val
    return render(request,'order/order_detail_accessuar.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_delete(request,id):
    order = Order.objects.get(id = id)
    order.delete()
    return redirect('order')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_delete_pvc(request,id):
    order = OrderPVX.objects.get(id = id)
    order.delete()
    return redirect('order_pvc')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_delete_radiator(request,id):
    order = OrderRadiator.objects.get(id = id)
    order.delete()
    return redirect('order_radiator')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_delete_akp(request,id):
    order = OrderAKP.objects.get(id = id)
    order.delete()
    return redirect('order_akp')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_delete_prochiye(request,id):
    order = OrderProchiye.objects.get(id = id)
    order.delete()
    return redirect('order_prochiye')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def order_delete_accessuar(request,id):
    order = OrderACS.objects.get(id = id)
    order.delete()
    return redirect('order_accessuar')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def status_change_to_done(request,id):
    order = Order.objects.get(id = id)
    order.work_type =10
    order.save()
    return redirect('order')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def status_change_to_done_pvc(request,id):
    order = OrderPVX.objects.get(id = id)
    order.work_type =6
    order.save()
    return redirect('order_pvc')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def status_change_to_done_akp(request,id):
    order = OrderAKP.objects.get(id = id)
    order.work_type =6
    order.save()
    return redirect('order_akp')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def status_change_to_done_prochiye(request,id):
    order = OrderProchiye.objects.get(id = id)
    order.work_type =6
    order.save()
    return redirect('order_prochiye')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def status_change_to_done_radiator(request,id):
    order = OrderRadiator.objects.get(id = id)
    order.work_type =6
    order.save()
    return redirect('order_radiator')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def status_change_to_done_accessuar(request,id):
    order = OrderACS.objects.get(id = id)
    order.work_type =6
    order.save()
    return redirect('order_accessuar')


