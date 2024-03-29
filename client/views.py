from django.shortcuts import render
from django.http import JsonResponse
from aluminiy.models import ArtikulComponent
from pvc.models import ArtikulKomponentPVC ,NakleykaPvc
from norma.models import Nakleyka
from .models import Anod,Order
from django.contrib.auth.decorators import login_required
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from accounts.decorators import customer_only,moderator_only



class OrderSaveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(['hello',])    
    
    def post(self, request):
        data = dict(request.data)
        try:
            order = Order(data = {'table':data['data'][0],'name':data['name'][0]},owner=request.user,order_type =data['order_type'])
            order.save()
            msg = 'Ordered successfully!'
            stat = 201
            return Response({'msg':msg,'status':stat,'order_id':order.id})    
        except:
            msg ='Something went wrong.'
            stat =300
            return Response({'msg':msg,'status':stat,'order_id':None})    


@login_required(login_url='/accounts/login/')
@moderator_only
def moderator_check(request,id):
    order = Order.objects.get(id = id)
    context ={
        'order':order
    }
    return render(request,'client/moderator/index.html',context)


@login_required(login_url='/accounts/login/')
@customer_only
def order_update(request,id):
    return render(request,'client/customer/index.html')


@login_required(login_url='/accounts/login/')
@customer_only
def order_list(request):
    orders = Order.objects.filter(owner = request.user).order_by('-created_at')
    context ={
        'orders':orders
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
