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
    studentid = models.TextField()
    classroom_grade = models.TextField()
    classroom_room = models.TextField()
    prefix = models.TextField()
    name_eng = models.TextField()
    surname_eng = models.TextField()
    birthplace = models.TextField()
    birthprovince = models.TextField()
    bloodtype = models.TextField()
    nationality = models.TextField()
    ethenic = models.TextField()
    religion = models.TextField()
    language_main = models.TextField()
    language_other = models.TextField()
    latest_school = models.TextField()
    latest_school_province = models.TextField()

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