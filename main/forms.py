from django import forms
from .models import Book

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Name"}),
        label='Name'
        )
    
    email = forms.EmailField(label='Your Email')

    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Enter Your Message"}),
        label='Message'
        )  

    def clean_name(self):
        name = self.cleaned_data['name']

        for char in name:
            if char.isdigit():
                raise forms.ValidationError("Name should not contain numbers...")
        return name


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "price"]