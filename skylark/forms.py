from django import forms
from brasil.models import Post
from skylark.models import Settings
from skylark.models import SettingsBlog
from skylark.models import ContactSettings
from taggit.forms import TagField
# from django import newsforms
# from django.newsforms.widgets import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post



class SettingsForm(forms.ModelForm):

    class Meta:
        model = Settings


class SettingsBlogForm(forms.ModelForm):

    class Meta:
        model = SettingsBlog


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

class SettingsContactForm(forms.ModelForm):

    class Meta:
        model = ContactSettings
