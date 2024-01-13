from django.urls import path
from .views import history, filter_book, home, issue_book, return_book, book_details, review_book

urlpatterns = [
    path('history', history, name="history"),
    path('filter/<int:id>/', filter_book, name='filter_book'),
    path('', home, name='home'),
    path('issue_book/<int:id>/', issue_book, name='issue_book'),
    path('return_book/<int:id>/', return_book, name='return_book'),
    path('book_details/<int:id>/', book_details, name='book_details'),
    path('book_borrow/<int:id>/', issue_book, name='borrow_book'),
    path('review/<int:id>/', review_book, name='review_book')
]
