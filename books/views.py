from .models import Author, Review, Book
from .models import User
from django.shortcuts import redirect, render

def book(request, id):
    book=Book.objects.get(id=id)
    context={
        'book':book
    }
    print(id)
    return render(request, 'book.html', context)


def books(request):
    user = User.objects.filter(id=request.session['id'])
    if user:
        book_list=Book.objects.all()
        context={
            'user': user[0],
            'books':book_list
        }
        return render(request, 'books.html', context)
    return render(request, ("/"))

def add_book(request):
    if request.method =='POST':
        title = request.POST.get('title')
        author= 'test author'
        print(request.session['id'])
        user = User.objects.filter(id=request.session['id'])[0]
        new_author=None
        if not author.isnumeric():
            names= author.split(' ')
            new_author= Author.objects.create(first_name=names[0], last_name=names[1], created_by=user)
        else:
            new_author= Author.objects.get(id=author)[0]
        desc= request.POST.get('description')
        rating=request.POST.get('rating')
        new_review= Review.objects.create(desc=desc, rating=rating, posted_by=user)
        new_book= Book.objects.create(title=title, author=new_author, added_by=user)
        new_book.review.add(new_review)
        return redirect('/books')
    return render(request, 'add_book.html')
