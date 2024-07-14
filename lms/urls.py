from django.urls import path
from lms import views

urlpatterns = [
    path('', views.get_book, name='getBook'),
    path('add_user/', views.add_user, name='addUser'),
    path('add_author/', views.add_author, name='addAuthor'),
    path('add_book/',views.add_book, name='addBook'),
    path('delete_book/<str:id>',views.delete_book, name='deleteBook'),
    path('update_book/<str:id>',views.update_book, name='updateBook'),
    path('get_author/',views.get_author, name='getAuthor'),
    path('delete_author/<str:id>',views.delete_author, name='deleteAuthor'),
    path('update_author/<str:id>',views.update_author, name='updateAuthor'),
    path('books_written/<str:id>', views.books_written, name='booksWritten'),
    path('get_user/',views.get_user, name='getUser'),
    path('delete_user/<str:id>',views.delete_user, name='deleteUser'),
    path('update_user/<str:id>',views.update_user, name='updateUser'),
    path('books_borrowed/<str:id>', views.books_borrowed, name='booksBorrowed'),
]

