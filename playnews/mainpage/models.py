from django.db import models

# Create your models here.

class UserInfo(models.Model):
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

class NewsInfo(models.Model):
    newsid = models.AutoField(primary_key=True)
    cnt = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    date_first = models.CharField(max_length=45, blank=True, null=True)
    date_mod = models.CharField(max_length=45, blank=True, null=True)
    newspaper = models.CharField(max_length=45, blank=True, null=True)
    writer = models.CharField(max_length=45, blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    img_link = models.CharField(max_length=200, blank=True, null=True)
    img_alt = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "%s " %(self.newsid)
    class Meta:
        managed = False
        db_table = 'newsinfo'



