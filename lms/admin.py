from django.contrib import admin

from lms.models import Author, Book, User

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(User)