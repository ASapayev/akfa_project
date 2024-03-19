from django.shortcuts import render
from django.http import JsonResponse
from aluminiy.models import ArtikulComponent
from pvc.models import ArtikulKomponentPVC ,NakleykaPvc
from norma.models import Nakleyka
from .models import Anod
from django.contrib.auth.decorators import login_required
import time

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'client/index.html')

def waiter(request):
    time.sleep(600)
    return JsonResponse({'aa':'dfdfsf'})

@login_required(login_url='/accounts/login/')
def shablon_imzo_detail(request):
    if request.method =='POST':
        context ={
            'link':'https://mdm.akfagroup.com/'
        }
        return render(request,'client/created_link.html',context)
    else:
        return render(request,'client/shablonlar/aluminiy_imzo.html')

@login_required(login_url='/accounts/login/')
def shablon_savdo_detail(request):
    return render(request,'client/shablonlar/aluminiy_savdo.html')

@login_required(login_url='/accounts/login/')
def shablon_export_detail(request):
    return render(request,'client/shablonlar/aluminiy_export.html')

@login_required(login_url='/accounts/login/')
def shablon_pvc_export_detail(request):
    return render(request,'client/shablonlar/pvc_imzo.html')


@login_required(login_url='/accounts/login/')
def shablon_pvc_savdo_detail(request):
    return render(request,'client/shablonlar/pvc_savdo.html')

@login_required(login_url='/accounts/login/')
def shablon_pvc_export_savdo_detail(request):
    return render(request,'client/shablonlar/pvc_export.html')

@login_required(login_url='/accounts/login/')
def imzo_artikul_list(request):
    
    term = request.GET.get('term',None)
    if term:
        artikules = ArtikulComponent.objects.filter(artikul__icontains = term).values('id','artikul','system','combination','code_nakleyka')
    else:
        artikules = ArtikulComponent.objects.all()[:50].values('id','artikul','system','combination','code_nakleyka')
    return JsonResponse(list(artikules),safe=False)


@login_required(login_url='/accounts/login/')
def pvc_artikul_list(request):
    
    term = request.GET.get('term',None)
    if term:
        artikules = ArtikulKomponentPVC.objects.filter(artikul__icontains = term).values('id','artikul','component','component2','category','nazvaniye_sistem','camera','kod_k_component','iskyucheniye')
    else:
        artikules = ArtikulKomponentPVC.objects.all()[:50].values('id','artikul','component','component2','category','nazvaniye_sistem','camera','kod_k_component','iskyucheniye')
    return JsonResponse(list(artikules),safe=False)
    
    
    
@login_required(login_url='/accounts/login/')
def nakleyka_list(request):
    
    term = request.GET.get('term',None)
    if term:
        nakleyka_l = Nakleyka.objects.filter(код_наклейки__icontains = term).distinct("код_наклейки").values('id','код_наклейки')
    else:
        nakleyka_l = Nakleyka.objects.all().distinct("код_наклейки").values('id','код_наклейки')
        
    return JsonResponse(list(nakleyka_l),safe=False)

@login_required(login_url='/accounts/login/')
def nakleyka_list_pvc(request):
    
    term = request.GET.get('term',None)
    if term:
        nakleyka_l = NakleykaPvc.objects.filter(name__icontains = term).distinct("name").values('id','name','nadpis')
    else:
        nakleyka_l = NakleykaPvc.objects.all().distinct("name").values('id','name','nadpis')
        
    return JsonResponse(list(nakleyka_l),safe=False)

@login_required(login_url='/accounts/login/')
def anod_list(request):
    term = request.GET.get('term',None)
    if term:
        anod_l = Anod.objects.filter(code_sveta__icontains = term).distinct("code_sveta").values('id','code_sveta','tip_anod','sposob_anod')
    else:
        anod_l = Anod.objects.all().distinct("code_sveta").values('id','code_sveta','tip_anod','sposob_anod')
        
    return JsonResponse(list(anod_l),safe=False)
