from django.db import models

class UserList(models.Model):
    idcard = models.CharField(max_length=13)
    prefix = models.TextField(default=None)
    name = models.TextField()
    surname = models.TextField()
    gender = models.TextField()
    tel = models.TextField()
    email = models.TextField()
    birthdate = models.TextField()
    type = models.TextField()
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.idcard + ' ' + self.name + ' ' + self.surname

    #def save(self,*args,**kwargs):
    #    super().save()
class Info_Basic(models.Model):
    idcard = models.CharField(max_length=13)
    name_eng = models.TextField()
    surname_eng = models.TextField()
    religion = models.TextField()
    nationality = models.TextField()
    ethenicity = models.TextField()
    #picture = 

class Info_Address(models.Model):
    idcard = models.CharField(max_length=13)
    home_id = models.TextField()
    village_id = models.TextField()
    village_name = models.TextField()
    parish = models.TextField()
    alley = models.TextField()
    road = models.TextField()
    district = models.TextField()
    city = models.TextField()
    zip_code = models.TextField()
    level_address = models.TextField()