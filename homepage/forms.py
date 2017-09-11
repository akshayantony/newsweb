from django import forms
from homepage.models import News,Newsrelimage,Subscribe,Contactus
from django.forms import Textarea
# from multiupload.fields import MultiImageField

class SearchForm(forms.Form):
    search_field=forms.CharField(label='',max_length=150)

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

# class NewsImageForm(forms.ModelForm):
#
#      class Meta:
#          model=Newsrelimage
#          fields=['rel_news','img']




# class AddForm(forms.ModelForm):
#     first = MultiImageField(min_num=1, max_num=20)
#
#     class Meta:
#         model = Newsrelimage
#         fields = ['rel_news','first']
#
#         def save(self, commit=True):
#             first_images = self.cleaned_data.pop('first')
#             instance = super(AddForm, self).save()
#             for each in first_images:
#                 first = Image(image=each, profile=instance, is_first=True)
#                 first.save()
#
#             return instance
#
#