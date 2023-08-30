from django import forms
from django.core.validators import validate_email

from .models import Query, NewsLetter



class QueryForm(forms.ModelForm):
    email = forms.CharField(validators=[validate_email])
    class Meta:
        model = Query
        fields = ('name', 'email', 'subject', 'message')


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email',)
