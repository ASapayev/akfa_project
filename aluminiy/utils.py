
from .models import ArtikulComponent
import os

def fabrikatsiya_sap_kod(sap_kod,length):
    new =sap_kod.split(' ')
    for i in range(0,len(new)):
        if new[i].startswith('L'):
            new[i]=f'L{length}'
    return ' '.join(new)

def do_exist(artikules):
    return ArtikulComponent.objects.filter(artikul__in=artikules).count() == len(artikules)

def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)
            