from django.shortcuts import render
from django.http import JsonResponse
from aluminiy.models import ArtikulComponent
from norma.models import Nakleyka

# Create your views here.

def index(request):
    return render(request,'client/index.html')

def shablon_imzo_detail(request):
    return render(request,'client/shablonlar/aluminiy_imzo.html')

def shablon_savdo_detail(request):
    return render(request,'client/shablonlar/aluminiy_savdo.html')


def shablon_export_detail(request):
    return render(request,'client/shablonlar/aluminiy_export.html')

def shablon_pvc_export_detail(request):
    return render(request,'client/shablonlar/pvc_imzo.html')



def shablon_pvc_savdo_detail(request):
    return render(request,'client/shablonlar/pvc_savdo.html')

def shablon_pvc_export_savdo_detail(request):
    return render(request,'client/shablonlar/pvc_export.html')


def imzo_artikul_list(request):
    if request.is_ajax():
        term = request.GET.get('term',None)
        if term:
            artikules = ArtikulComponent.objects.filter(artikul__icontains = term).values('id','artikul','system','combination','code_nakleyka')
        else:
            artikules = ArtikulComponent.objects.all()[:50].values('id','artikul','system','combination','code_nakleyka')
        return JsonResponse(list(artikules),safe=False)
    
    
    return JsonResponse(list(artikules),safe=False)

def nakleyka_list(request):
    if request.is_ajax():
        term = request.GET.get('term',None)
        if term:
            nakleyka_l = Nakleyka.objects.filter(код_наклейки__icontains = term).distinct("код_наклейки").values('id','код_наклейки')
        else:
            nakleyka_l = Nakleyka.objects.all().distinct("код_наклейки").values('id','код_наклейки')
            
        return JsonResponse(list(nakleyka_l),safe=False)
    else:
        return JsonResponse({'a':'b'})