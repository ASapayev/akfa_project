from django.db import models

# Create your models here.


class MatrixFile(models.Model):
  file =models.FileField(upload_to='uploads/matrix/downloads/',max_length=500)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)


class TexcartaMatrixFile(models.Model):
  file =models.FileField(upload_to='uploads/matrix/downloads/',max_length=500)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)


class MatrixBase(models.Model):
    sapcode =models.CharField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class RazlovkaMatrix(models.Model):
    nsapkode = models.CharField(max_length = 50,blank=True,null=True)
    nkrat = models.CharField(max_length = 50,blank=True,null=True)
    tchsapkode = models.CharField(max_length = 50,blank=True,null=True)
    tchkrat = models.CharField(max_length = 50,blank=True,null=True)
    fchsapkode = models.CharField(max_length = 50,blank=True,null=True)
    fchkrat = models.CharField(max_length = 50,blank=True,null=True)
    zsapkode = models.CharField(max_length = 50,blank=True,null=True)
    zkrat = models.CharField(max_length = 50,blank=True,null=True)
    shsapkode = models.CharField(max_length = 50,blank=True,null=True)
    shkrat = models.CharField(max_length = 50,blank=True,null=True)
    tsapkode = models.CharField(max_length = 50,blank=True,null=True)
    tkrat = models.CharField(max_length = 50,blank=True,null=True)
    fsapkode = models.CharField(max_length = 50,blank=True,null=True)
    fkrat = models.CharField(max_length = 50,blank=True,null=True)
    edmsapkode = models.CharField(max_length = 50,blank=True,null=True)
    edmkrat = models.CharField(max_length = 50,blank=True,null=True)
    sapkode7 = models.CharField(max_length = 50,blank=True,null=True)
    krat7 = models.CharField(max_length = 50,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)