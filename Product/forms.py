from django import forms
from .models import ProductReview

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = ProductReview
        fields = ['product_rate', 'name', 'surname', 'review']
        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'review': "Review"
        }
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your name",
                }
            ),
            'surname' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your surname"
                }
            ),
            'review' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 5,
                    'placeholder' :"Enter your Review"
                }
            )
        }

