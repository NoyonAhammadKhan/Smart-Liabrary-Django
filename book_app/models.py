from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from user_app.models import UserAccount
from .constants import TYPE
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name_plural = "categories"


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books')
    borrowing_price = models.DecimalField(
        default=0, max_digits=12, decimal_places=2)
    categories = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title}"


class Review(models.Model):
    review = models.CharField(max_length=300)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='reviews')


class BookIssueRetrunHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,)
    account = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True)
    borrowing_price = models.DecimalField(
        default=0, max_digits=12, decimal_places=2)
    before_balance = models.DecimalField(
        default=0, max_digits=12, decimal_places=2)
    after_balance = models.DecimalField(
        default=0, max_digits=12, decimal_places=2)
    type = models.IntegerField(choices=TYPE)
    is_returned = models.BooleanField(default=False)
