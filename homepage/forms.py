from django import forms
from homepage.models import News,Newsrelimage,Subscribe,Contactus
from django.forms import Textarea

class SearchForm(forms.Form):
    search_field=forms.CharField(label='Search keyword',max_length=150, required=True)

    class Meta:
        fields=['search_field',]

class NewsForm(forms.ModelForm):

    class Meta:
        model=News
        fields=['title','content','created_date','category']

class NewsImageForm(forms.ModelForm):
    class Meta:
        model = Newsrelimage
        fields = ['img']


class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields = ['Email']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        fields="__all__"
