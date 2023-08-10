from django.db import models
from accounts.models import User
import jsonfield


STATUS_CHOICES =(
    (1,'ON HOLD'),
    (2,'ON PROCESS'),
    (3,'CANCEL'),
    (4,'DONE')
)
WORK_TYPE_CHOICES =(
    (1,'SAP CODE CREATING'),
    (2,'SAP CODE CREATING LACKS'),
    (3,'TEXT CREATING'),
    (4,'TEXT CREATING LACKS'),
    (5,'NORMA'),
    (6,'NORMA CREATING LACKS'),
    (7,'TEXCARTA'),
    (8,'VI')
)
class Order(models.Model):
    title = models.CharField(max_length=150)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=1)
    work_type =models.SmallIntegerField(choices=WORK_TYPE_CHOICES,default=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    current_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='on_time_worker')
    aluminiy_worker = models.ForeignKey(User,models.CASCADE,blank=True,null=True,related_name='aluminiy_work')
    alumin_wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='aluminiy_work_wrong')
    norma_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='norma_work')
    norma_wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='norma_work_wrong')
    texcarta_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='texcarta_work')
    vi_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='vi_work')
    paths = jsonfield.JSONField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)