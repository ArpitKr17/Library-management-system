from django import forms
from .models import Author, User, Book
    
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birthdate']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'})
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name']
        

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'published_date', 'author', 'user_borrowed']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }
       