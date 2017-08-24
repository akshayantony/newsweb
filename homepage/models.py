from django.db import models
from django.utils import timezone

class News(models.Model):
    author = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def created_d(self):
        self.created_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title