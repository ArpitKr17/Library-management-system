from django.shortcuts import render, redirect
from lms.models import Book, Author, User
from .forms import AuthorForm, UserForm, BookForm
from lms.signals import book_add_signal, book_borrow_signal

def home(request):
    return render(request, 'homepage.html')

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getBook')
    else:
        form = AuthorForm()
    context={
        'form':form,
        'form_name':'Author'
    }
    return render(request, 'form.html', context=context)

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getBook')
    else:
        form = UserForm()
         
    context={
        'form':form,
        'form_name':'User'
    }
    return render(request, 'form.html', context=context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            book_add_signal.send(sender=Book)
            return redirect('getBook')
    else:
        form = BookForm()
         
    context={
        'form':form,
        'form_name':'Book'
    }
    return render(request, 'form.html', context=context)

def get_book(request):
    year=request.GET.get('search') 
    if year:
        books=Book.objects.select_related('user_borrowed','author').filter(published_date__year=year)
    else:
        books = Book.objects.all()
    
    context={
        'books':books
    }
    return render(request, 'homepage.html', context=context)

def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('getBook')

def update_book(request, id):
    book=Book.objects.get(id=id)
    user_borrowed=book.user_borrowed.id
    if request.method=='POST':
        updated_user_borrowed=request.POST['user_borrowed']
        if updated_user_borrowed!=user_borrowed:
            book_borrow_signal.send(sender=Book)
        form=BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('getBook')
    else:
        form=BookForm(instance=book)
        context={
        'form':form,
        'form_name':'Book'
         }
    return render(request, 'form.html', context=context)

def get_author(request):
    authors=Author.objects.all()
    context={
        'authors':authors
    }
    return render(request, 'author.html', context=context)

def delete_author(request,id):
    author=Author.objects.get(id=id)
    author.delete()
    return redirect('getAuthor')

def update_author(request, id):
    author=Author.objects.get(id=id)
    
    if request.method=='POST':
        form=AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('getAuthor')
    else:
        form=AuthorForm(instance=author)
        context={
        'form':form,
        'form_name':'Author'
         }
    return render(request, 'form.html', context=context)

def books_written(request,id):
    author=Author.objects.get(id=id)
    books_written=author.books.all()
    context={
        'books':books_written
    }
    return render(request, 'homepage.html', context=context)

def get_user(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user.html', context=context)

def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('getUser')

def update_user(request, id):
    user = User.objects.get(id=id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('getUser')
    else:
        form = UserForm(instance=user)
        context = {
            'form': form,
            'form_name': 'User'
        }
    return render(request, 'form.html', context=context)

def books_borrowed(request,id):
    user=User.objects.get(id=id)
    books_borrowed=user.books_borrowed.all()
    context={
        'books':books_borrowed
    }
    return render(request, 'homepage.html', context=context)
