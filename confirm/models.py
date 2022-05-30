from django.db import models

class UserList(models.Model):
    idcard = models.CharField(max_length=13)
    name = models.TextField()
    surname = models.TextField()
    gender = models.TextField()
    tel = models.TextField()
    email = models.TextField()
    birthdate = models.TextField()
    type = models.TextField()
    activated = models.BooleanField(default=False)

    #def save(self,*args,**kwargs):
    #    super().save()