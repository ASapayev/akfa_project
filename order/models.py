from django.db import models
from accounts.models import User



STATUS_CHOICES =(
    (1,'ON HOLD'),
    (2,'ON PROCESS'),
    (3,'CANCEL'),
    (4,'DONE')
)
WORK_TYPE_CHOICES =(
    (1,'ON HOLD'),
    (2,'SAP CODE CREATING'),
    (3,'SAP CODE CREATING LACKS'),
    (4,'TEXT CREATING'),
    (5,'TEXT CREATING LACKS'),
    (6,'NORMA'),
    (7,'NORMA CREATING LACKS'),
    (8,'TEXCARTA'),
    (9,'VI'),
    (10,'DONE')
)
ORDER_TYPE_CHOICES =(
    (1,'ОБЫЧНЫЙ'),
    (2,'ТЕРМО')
)
class Order(models.Model):
    title = models.CharField(max_length=150)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=1)
    work_type =models.SmallIntegerField(choices=WORK_TYPE_CHOICES,default=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    current_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='on_time_worker')
    aluminiy_worker = models.ForeignKey(User,models.CASCADE,blank=True,null=True,related_name='aluminiy_work')
    alumin_wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='aluminiy_work_wrong')
    alumin_text_wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='aluminiy_text_work_wrong')
    norma_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='norma_work')
    norma_wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='norma_work_wrong')
    texcarta_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='texcarta_work')
    vi_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='vi_work')
    paths = models.JSONField(null=True,blank=True,default=dict)
    order_type = models.SmallIntegerField(choices=ORDER_TYPE_CHOICES,default=1)
    order_name = models.CharField(max_length=50,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

STATUS_CHOICES_PVC =(
     (1,'ON HOLD'),
    (2,'ON PROCESS'),
    (3,'CANCEL'),
    (4,'DONE')
)

WORK_TYPE_CHOICES_PVC =(
    (1,'ON HOLD'),
    (2,'SAP CODE CREATING'),
    (3,'SAP CODE CREATING LACKS'),
    (4,'TEXT CREATING'),
    (5,'TEXT CREATING LACKS'),
    (6,'DONE')
)
ORDER_TYPE_CHOICES_PVC =(
    (1,'ЛАМ'),
    (2,'БЕЗ ЛАМ')
)

class OrderPVX(models.Model):
    title = models.CharField(max_length=150)
    status = models.SmallIntegerField(choices=STATUS_CHOICES_PVC,default=1)
    work_type =models.SmallIntegerField(choices=WORK_TYPE_CHOICES_PVC,default=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    current_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='on_time_worker_pvc')
    pvc_worker = models.ForeignKey(User,models.CASCADE,blank=True,null=True,related_name='pvc_work')
    pvc_wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='pvc_work_wrong')
    paths = models.JSONField(null=True,blank=True,default=dict)
    order_type = models.SmallIntegerField(choices=ORDER_TYPE_CHOICES_PVC,default=1)
    order_name = models.CharField(max_length=50,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)