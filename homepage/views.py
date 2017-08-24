from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from homepage.models import News

def news_list(request):
    return render(request,'homepage/news_list.html',{})

class NewsView(generic.ListView):
    template_name = 'homepage/news_list.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        return News.objects.order_by('created_date')