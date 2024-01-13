from django.db import models
from django.contrib.auth.models import User
from .constants import DEPARTMENT_TYPE, FACULTY_TYPE, TRANSACTION_TYPE
# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(
        User, related_name='account', on_delete=models.CASCADE, related_query_name='')
    account_no = models.IntegerField(unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.account_no)


class UserDepartment(models.Model):
    user = models.OneToOneField(
        User,  on_delete=models.CASCADE)
    department = models.CharField(max_length=10, choices=DEPARTMENT_TYPE)
    faculty = models.CharField(max_length=19, choices=FACULTY_TYPE)
