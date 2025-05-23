from django.db import models
import uuid

code = uuid.uuid4().hex[:10]

# Create your models here.
class Myusers(models.Model):
    username:str = models.CharField(max_length=100)
    userId:str = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=10,default=code)
    referred_by:str = models.CharField(max_length=100,default=[])
    referred_users:str = models.CharField(max_length=100,default=None)
    # balance:int =  models.DecimalField()
    

    def __str__(self):
        return f'{self.username, self.userId, self.referral_code, self.referred_by, self.referred_users}'