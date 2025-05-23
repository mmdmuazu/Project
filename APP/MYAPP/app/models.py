from django.db import models

# Create your models here.

class MyUsers(models.Model):
    fullName = models.CharField(max_length = 100)#default="Amir")
    username = models.CharField(max_length = 100)#default = 'Amir')
    userEmail = models.EmailField(max_length = 100) #default='amir@gmail.com')
    userPassword = models.CharField(max_length = 100) #default = '12345678')
    verify = models.BooleanField()

    def __str__(self):
        return f'{self.username} {self.userEmail} {self.fullName} {self.userPassword} {self.verify}'