from django.db import models
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import *
from django.dispatch import receiver
from django.utils import timezone, six

from django.contrib.auth.models import User,AbstractBaseUser,AbstractUser
# Create your models here.


#doctor user
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,null=True)
    specialty=models.CharField(max_length=250)
    establishment=models.CharField(max_length=100)
    #phone_establishment=models.CharField(max_length=15,)
    photo=models.FileField(upload_to='images/', null=True, blank=True, verbose_name="")

    def get_teen_mammographys(self):
        list = Mammography.objects.raw("select m.id,m.user_id,m.momography from collection_donnees_Mammography m where m.id not in (select d.mammography_id from collection_donnees_Diagnostic d where D.user_id =="+str(self.id)+")")[:10]
        return list

    #TODO:: -last 10 diagnostics - all diagnostics - all mammography added






#mamography

class Mammography(models.Model):
    user=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    momography=models.FileField(upload_to='images/', null=True, verbose_name="")


#diagnostic
class Diagnostic(models.Model):
    mammography=models.ForeignKey(Mammography,on_delete=models.CASCADE)
    user=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    rate=models.FloatField()
    comment=models.TextField()
    date=models.DateField()




