from django.contrib import admin
from .models import UserAccount, User, UserDepartment
# Register your models here.
admin.site.register(UserDepartment)
admin.site.register(UserAccount)
