from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    birthdate=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name +" " + self.last_name
    
class User(models.Model):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name +" " + self.last_name
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    isbn=models.CharField(max_length=100)
    published_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    user_borrowed=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='books_borrowed')
    
    def __str__(self):
        return self.title
    
    
    