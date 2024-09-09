from django.core.management.base import BaseCommand
from norma.models import Norma,Kraska
from django.http import JsonResponse

class Command(BaseCommand):
    help = 'Norma check for existing.'

    def handle(self, *args, **kwargs):
        a=self.norma_for_test()
        # print(a)
        
    def norma_for_test(self):
        # normas = Norma.objects.all().values_list("компонент_1","компонент_2","компонент_3",'артикул')
        # normass =[]
        # for norm in normas:
        #     for n in norm:
        #         if n !='0' and n!='nan':
        #             normass.append(n)
        # norma_unique =set(normass)
        kraskas = Kraska.objects.all().values_list('код_краски_в_профилях',flat=True)
        # print(kraskas)
        return 1