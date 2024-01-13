from django.shortcuts import render, redirect
from .models import Category, Book, BookIssueRetrunHistory, Review
from user_app.models import UserAccount
from .forms import ReviewForm
# Create your views here.


def home(request):
    books = Book.objects.all()
    books_count = books.count()
    category = 'all'
    categories = Category.objects.all()
    print(categories)
    print(books)
    context = {'books': books, 'books_count': books_count,
               'category': category, 'categories': categories, }
    return render(request, 'home.html', context)


def filter_book(request, id):
    category = Category.objects.get(pk=id)
    books = Book.objects.filter(categories=category)
    books_count = books.count()
    categories = Category.objects.all()
    return render(request, 'home.html', {'books': books, 'books_count': books_count, 'category': category.category, 'categories': categories})


def issue_book(request, id):
    book = Book.objects.get(pk=id)
    user = request.user
    print(user)
    account = UserAccount.objects.get(user=user)
    print(f"acc {account}")
    borrowing_price = book.borrowing_price

    if account.balance > borrowing_price:
        before_balance = account.balance
        account.balance -= borrowing_price
        account.save()
        after_balance = account.balance
        type = 1
        book_issue = BookIssueRetrunHistory()
        book_issue.account = account
        book_issue.book = book
        book_issue.borrowing_price = borrowing_price
        book_issue.before_balance = before_balance
        book_issue.after_balance = after_balance
        book_issue.type = type
        print(f"book_issue {book_issue}")
        book_issue.save()
        return redirect('history')
    else:
        return redirect('deposit')


def return_book(request, id):
    book_return_history = BookIssueRetrunHistory.objects.get(pk=id)
    book_return_history.is_returned = True
    book_return_history.save()
    book = book_return_history.book
    user = request.user
    account = UserAccount.objects.get(user=user)
    borrowing_price = book.borrowing_price
    before_balance = account.balance
    account.balance += borrowing_price
    account.save()
    after_balance = account.balance
    type = 2
    book_issue = BookIssueRetrunHistory()
    book_issue.account = account
    book_issue.book = book
    book_issue.borrowing_price = borrowing_price
    book_issue.before_balance = before_balance
    book_issue.after_balance = after_balance
    book_issue.type = type
    book_issue.save()
    return redirect('history')


def history(request):
    all_history = BookIssueRetrunHistory.objects.all()
    return render(request, 'book_issue_history.html', {'all_history': all_history})


def book_details(request, id):
    book = Book.objects.get(pk=id)
    reviews = Review.objects.filter(book=book)
    print(reviews)
    if request.user.is_authenticated:
        account = UserAccount.objects.get(user=request.user)
        is_issued = BookIssueRetrunHistory.objects.filter(
            account=account, book=book)
        if is_issued:
            is_issued = True
        else:
            is_issued = False
    else:
        return redirect('login')
    return render(request, 'book_details.html', {'book': book, 'is_issued': is_issued, 'reviews': reviews})


def review_book(request, id):
    book = Book.objects.get(pk=id)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            book_form = form.save(commit=False)
            book_form.book = book
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
        return render(request, 'book_review.html', {'form': form})
