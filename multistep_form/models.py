from django.db import models

class MultiStepForm(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phno = models.CharField(max_length=255)
    phno_2 = models.CharField(max_length=255)
    photo = models.FileField()
    sign = models.FileField()
    objects = models.Manager()

# class MultiStepForm(models.Model):
#     id=models.AutoField(primary_key=True)
#     fname=models.CharField(max_length=255,default="{Nothing Here}")
#     lname=models.CharField(max_length=255,default="{Nothing Here}")
#     phone=models.CharField(max_length=255,default="{Nothing Here}")
#     twitter=models.CharField(max_length=255,default="{Nothing Here}")
#     facebook=models.CharField(max_length=255,default="{Nothing Here}")
#     gplus=models.CharField(max_length=255,default="{Nothing Here}")
#     email=models.CharField(max_length=255,default="{Nothing Here}")
#     password=models.CharField(max_length=255,default="{Nothing Here}")
#     objects=models.Manager()