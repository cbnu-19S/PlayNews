from django.contrib import admin

# Register your models here.
from .models import Userinfo,Newsinfo

admin.site.register(Userinfo)
admin.site.register(Newsinfo)