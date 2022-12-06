from django.db import models

# Create your models here.

class UserInfo(models.Model):
    userssn=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    userid=models.CharField(max_length=20)
    userpw=models.CharField(max_length=20)
    useremail = models.CharField(max_length=30)
    userAddress = models.CharField(max_length=50)
    userPhone = models.CharField(max_length=20)

    def __str__(self):
        return "%s " %(self.username)

    class Meta:
        db_table="userinfo"

# class ArticleInfo(models.Model):



