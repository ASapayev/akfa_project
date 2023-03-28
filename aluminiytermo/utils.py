
from .models import ArtikulComponent

def fabrikatsiya_sap_kod(sap_kod,length):
    new =sap_kod.split(' ')
    for i in range(0,len(new)):
        if new[i].startswith('L'):
            new[i]=f'L{length}'
    return ' '.join(new)

def do_exist(artikules):
    return ArtikulComponent.objects.filter(artikul__in=artikules).count() == len(artikules)
            