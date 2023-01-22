from django import forms
from .models import BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'comment']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'comment': "Comment"
        }
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your name",
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            ),
            'comment' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 5,
                    'placeholder' :"Enter your Review Subjects"
                }
            )
        }
