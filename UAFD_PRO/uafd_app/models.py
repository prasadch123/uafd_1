from django.db import models
from django.contrib.auth.models import User
class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    aadhar=models.CharField(max_length=100)
    userid=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Application_Form(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    father_name=models.CharField(max_length=100,null=True)
    aadhar_number=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100,null=True)
    date=models.DateField(max_length=100,null=True)
    caste=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    district=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)
    education=models.CharField(max_length=100,null=True)
    technical=models.CharField(max_length=50,null=True)
    work_experiance=models.CharField(max_length=50,null=True)
    job_applying=models.CharField(max_length=100,null=True)
    job_state=models.CharField(max_length=100,null=True)
    job_district=models.CharField(max_length=100,null=True)
    job_mandal=models.CharField(max_length=100,null=True)
    job_village=models.CharField(max_length=100,null=True,blank=True)
    photo=models.ImageField(null=True,blank=True,)
    signature=models.ImageField(null=True,blank=True)
    fee=models.CharField(max_length=100,null=True)


class Transaction_Id(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Transaction_Id=models.CharField(max_length=100,null=True)
