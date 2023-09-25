from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request, dt=None):
    template = 'books/books_list.html'
    context = {}
    if dt:
        books = Book.objects.filter(pub_date=dt)
        books_less = Book.objects.filter(pub_date__lt=dt).order_by("-pub_date").first()
        books_greater = Book.objects.filter(pub_date__gt=dt).order_by("pub_date").first()
        if books_less:
            books_less.pub_date = str(books_less.pub_date)
            context['books_less'] = books_less
        if books_greater:
            books_greater.pub_date = str(books_greater.pub_date)
            context['books_greater'] = books_greater
    else:
        books = Book.objects.all()
    for book in books:
        book.pub_date = str(book.pub_date)
    context['books'] = books

    return render(request, template, context)
