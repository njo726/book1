from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'status', 'price', 'image_url']

    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'عنوان الكتاب',
                'class': 'form-control',
                'type': 'text'
            }
        )
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'المؤلف',
                'class': 'form-control',
                'type': 'text'
            }
        )
    )
    genre = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'النوع',
                'class': 'form-control',
                'type': 'text'
            }
        )
    )
    status = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'الحالة',
                'class': 'form-control',
                'type': 'text'
            }
        )
    )
    price = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'السعر',
                'class': 'form-control',
                'type': 'text'
            }
        )
    )
    image_url = forms.URLField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'الصورة',
                'class': 'form-control',
                'id': 'totalrente',
                'type': 'text'
            }
        )
    )
