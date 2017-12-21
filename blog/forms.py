from django import forms

from blog.models import comments


class commentsForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField()
