from django import forms
from cheryl.models import Page, Content


class PageForm(forms.ModelForm):

    class Meta:
        model = Page


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
