from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text',)
        


class Contactme(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    subject=forms.CharField(max_length=100)
    message=forms.TimeField()
    def __str__(self):
        return self.subject
