from django.db import models

# Create your models here.

class Userinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    userpw = models.CharField(max_length=20)
    useremail = models.CharField(max_length=30)
    useraddress = models.CharField(db_column='userAddress', max_length=50)  # Field name made lowercase.
    userphone = models.CharField(db_column='userPhone', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinfo'


    def __str__(self):
        return "%s " %(self.username)


class Newsinfo(models.Model):
    newsid = models.AutoField(primary_key=True)
    cnt = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    date_first = models.CharField(max_length=45, blank=True, null=True)
    date_mod = models.CharField(max_length=45, blank=True, null=True)
    newspaper = models.CharField(max_length=45, blank=True, null=True)
    writer = models.CharField(max_length=45, blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    img_link = models.TextField(blank=True, null=True)
    img_alt = models.TextField(blank=True, null=True)
    keyword = models.CharField(max_length=45, blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsinfo'


