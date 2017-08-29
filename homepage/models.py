from django.db import models
from django.utils import timezone

class NewsCategories(models.Model):
    cname = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.cname

class News(models.Model):
    author = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(NewsCategories, null=True)
    images = models.ImageField(upload_to="modelimages/",blank=True,null=True)
    def created_d(self):
        self.created_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
