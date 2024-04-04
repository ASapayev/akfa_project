from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from aluminiy.models import ArtikulComponent
from pvc.models import ArtikulKomponentPVC ,NakleykaPvc
from norma.models import Nakleyka
from .models import Anod,Order,OrderDetail
from django.contrib.auth.decorators import login_required
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from accounts.decorators import customer_only,moderator_only,allowed_users
from django.core.paginator import Paginator
import json
from .forms import OrderFileForm



class OrderSaveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print('come to get')
        return Response(['hello',])    
    
    def post(self, request):
        data = request.data.get('data',None)
        name = request.data.get('name',None)
        order_type = request.data.get('order_type',None)
        res = json.loads(data)
        try:
            order = Order(data = {'name':name,'data':res},owner=request.user,order_type = order_type)
            order.save()
            order_detail = OrderDetail(order=order,owner=request.user)
            order_detail.save()
            return Response({'msg':'Ordered successfully!','status':201,'order_id':order.id})    
        except:
            return Response({'msg':'Something went wrong.','status':300,'order_id':None})    


@login_required(login_url='/accounts/login/')
@moderator_only
def order_list_for_moderator(request):
    orders = Order.objects.all()

    paginator = Paginator(orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)


    context ={
        'orders':page_obj
    }
    return render(request,'client/moderator/order_list.html',context)

@login_required(login_url='/accounts/login/')
@moderator_only
def moderator_check(request,id):
    if request.method =='POST':
        data =request.POST.copy()
        owner =request.user
        order = Order.objects.get(id=id)
        order.status = data.get('status',1)
        order.save()
        data['owner'] = owner
        data['order'] = order
        form = OrderFileForm(data,request.FILES)
        if form.is_valid():
            form.save()
            order_details = OrderDetail.objects.filter(order = order)
            context ={
                'status':str(order.status),
                'order_type':order.order_type,
                'data':json.dumps(order.data),
                'order_details':order_details
            }
            return render(request,'client/moderator/order_detail.html',context)
        else:
            return JsonResponse({'form':form.errors})
    else:
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
        context ={
            'status':str(order.status),
            'order_type':order.order_type,
            'data':json.dumps(order.data),
            'order_details':order_details
        }
        return render(request,'client/moderator/order_detail.html',context)


@login_required(login_url='/accounts/login/')
@customer_only
def order_update(request,id):
    return render(request,'client/customer/update.html')


@login_required(login_url='/accounts/login/')
@customer_only
def order_detail(request,id):
    if request.method =='POST':
        data =request.POST.copy()
        owner =request.user
        order = Order.objects.get(id=id)
        order.status = data.get('status',1)
        order.save()
        data['owner'] = owner
        data['order'] = order
        form = OrderFileForm(data,request.FILES)
        if form.is_valid():
            form.save()
            order_details = OrderDetail.objects.filter(order = order)
            context ={
                'status':str(order.status),
                'order_type':order.order_type,
                'data':order.data,
                'order_details':order_details
            }
            return render(request,'client/customer/order_detail.html',context)
        else:
            return JsonResponse({'form':form.errors})
    else:
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
        context ={
            'status':str(order.status),
            'order_type':order.order_type,
            'data':order.data,
            'order_details':order_details
        }
        return render(request,'client/customer/order_detail.html',context)

   


@login_required(login_url='/accounts/login/')
@customer_only
def order_list(request):
    orders = Order.objects.filter(owner = request.user).order_by('-created_at')
    paginator = Paginator(orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context ={
        'orders':page_obj
    }
    return render(request,'client/customer/order_list.html',context)





#################
@login_required(login_url='/accounts/login/')
@customer_only
def index(request):
    return render(request,'client/index.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_imzo_detail(request):
    if request.method =='POST':
        context ={
            'link':'https://mdm.akfagroup.com/'
        }
        return render(request,'client/created_link.html',context)
    else:
        return render(request,'client/shablonlar/aluminiy_imzo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_savdo_detail(request):
    return render(request,'client/shablonlar/aluminiy_savdo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_export_detail(request):
    return render(request,'client/shablonlar/aluminiy_export.html')


@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_export_detail(request):
    return render(request,'client/shablonlar/accessuar_imzo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_savdo_detail(request):
    return render(request,'client/shablonlar/accessuar_savdo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_export_savdo_detail(request):
    return render(request,'client/shablonlar/accessuar_export.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_export_detail(request):
    return render(request,'client/shablonlar/pvc_imzo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_savdo_detail(request):
    return render(request,'client/shablonlar/pvc_savdo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_export_savdo_detail(request):
    return render(request,'client/shablonlar/pvc_export.html')

@login_required(login_url='/accounts/login/')
@customer_only
def imzo_artikul_list(request):
    
    term = request.GET.get('term',None)
    if term:
        artikules = ArtikulComponent.objects.filter(artikul__icontains = term).values('id','artikul','system','combination','code_nakleyka')
    else:
        artikules = ArtikulComponent.objects.all()[:50].values('id','artikul','system','combination','code_nakleyka')
    return JsonResponse(list(artikules),safe=False)


@login_required(login_url='/accounts/login/')
@customer_only
def pvc_artikul_list(request):
    
    term = request.GET.get('term',None)
    if term:
        artikules = ArtikulKomponentPVC.objects.filter(artikul__icontains = term).values('id','artikul','component','component2','category','nazvaniye_sistem','camera','kod_k_component','iskyucheniye')
    else:
        artikules = ArtikulKomponentPVC.objects.all()[:50].values('id','artikul','component','component2','category','nazvaniye_sistem','camera','kod_k_component','iskyucheniye')
    return JsonResponse(list(artikules),safe=False)
    
    
    
@login_required(login_url='/accounts/login/')
@customer_only
def nakleyka_list(request):
    
    term = request.GET.get('term',None)
    if term:
        nakleyka_l = Nakleyka.objects.filter(код_наклейки__icontains = term).distinct("код_наклейки").values('id','код_наклейки')
    else:
        nakleyka_l = Nakleyka.objects.all().distinct("код_наклейки").values('id','код_наклейки')
        
    return JsonResponse(list(nakleyka_l),safe=False)

@login_required(login_url='/accounts/login/')
@customer_only
def nakleyka_list_pvc(request):
    
    term = request.GET.get('term',None)
    if term:
        nakleyka_l = NakleykaPvc.objects.filter(name__icontains = term).distinct("name").values('id','name','nadpis')
    else:
        nakleyka_l = NakleykaPvc.objects.all().distinct("name").values('id','name','nadpis')
        
    return JsonResponse(list(nakleyka_l),safe=False)

@login_required(login_url='/accounts/login/')
@customer_only
def anod_list(request):
    term = request.GET.get('term',None)
    if term:
        anod_l = Anod.objects.filter(code_sveta__icontains = term).distinct("code_sveta").values('id','code_sveta','tip_anod','sposob_anod')
    else:
        anod_l = Anod.objects.all().distinct("code_sveta").values('id','code_sveta','tip_anod','sposob_anod')
        
    return JsonResponse(list(anod_l),safe=False)
