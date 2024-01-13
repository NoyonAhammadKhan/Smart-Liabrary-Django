from django.contrib import admin
from .models import Book, BookIssueRetrunHistory, Review, Category
# Register your models here.
admin.site.register(Book)
admin.site.register(BookIssueRetrunHistory)
admin.site.register(Review)
admin.site.register(Category)
