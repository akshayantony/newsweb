from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template import loader, Context
from django.http import HttpResponse
from django.dispatch import receiver

class NewsCategories(models.Model):
    cname = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.cname

@python_2_unicode_compatible
class News(models.Model):
    author = models.CharField(max_length=100,blank=True)
    title = models.TextField()
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(NewsCategories, null=True)

    def created_d(self):
        self.created_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('homepage:newsdetail', kwargs={'pk': self.pk})

@python_2_unicode_compatible
class Newsrelimage(models.Model):
    rel_news = models.ForeignKey(News,on_delete=models.CASCADE,related_name="images")
    img=models.FileField(upload_to="modelimages/",blank=True,null=True)

    def __str__(self):
        return self.rel_news.title

class Subscribe(models.Model):
    Email=models.EmailField(unique=True)
    token=models.CharField(max_length=100,null=True)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.Email

@receiver(post_save, dispatch_uid="news_update", sender=News)
def subscription_handler(instance,**kwargs):
    subscribers=Subscribe.objects.filter(is_active=True)
    newsletter_temp=loader.get_template('homepage/newsletter.html')
    context={ 'news':instance }
    message=newsletter_temp.render(context)
    send_mail(
        'SayoneNews! News Published ! %s' % kwargs['sender'].title,
        message,
        'dailycirclenews@gmail.com',
        [sub for sub in subscribers ],
        fail_silently=False,
    )
    return HttpResponse("Entered Signal")


post_save.connect(subscription_handler, sender=News, dispatch_uid="subscription_handler")

@python_2_unicode_compatible
class Contactus(models.Model):
    name=models.CharField(max_length=100,blank=True)
    email=models.EmailField()
    subject=models.CharField(max_length=200,blank=True)
    content=models.TextField(blank=True)

    def __str__(self):
        return self.name




# class Image(models.Model):
#     image = models.FileField(upload_to="modelimages/",blank=True,null=True)
#     profile = models.ForeignKey(News,on_delete=models.CASCADE, related_name='images')
#     is_first = models.BooleanField(default=False)
#     is_second = models.BooleanField(default=False)