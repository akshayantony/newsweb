from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from homepage.models import News,NewsCategories

class NewsView(generic.ListView):
    template_name = 'homepage/news_list.html'
    context_object_name = 'latest_news_list'
    queryset=News.objects.order_by('created_date')

   # def get_queryset(self):
    #    return News.objects.order_by('created_date')
    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['categ_news'] = NewsCategories.objects.all()
        if self.kwargs:
            context['username'] = self.kwargs['username']
        return context

class DetailView(generic.DetailView):
    model=News
    context_object_name='news'
    template_name= 'homepage/detail_news.html'

class CategoryView(generic.ListView):
    template_name = 'homepage/newscategory_list.html'
    context_object_name = 'categ_news_list'

    def get_queryset(self,**kwargs):
        return News.objects.filter(category=self.kwargs['categ'])
