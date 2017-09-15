from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.views import generic, View
from homepage.models import News,NewsCategories,Newsrelimage
from homepage.forms import SearchForm,NewsForm ,NewsImageForm,SubscribeForm,ContactForm
from homepage.models import Subscribe
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class NewsView(generic.ListView):
    template_name = 'homepage/news_list.html'
    context_object_name = 'latest_news_list'
    paginate_by = 3

    def get_queryset(self):
        return News.objects.all().order_by('-created_date')

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['categ_news'] = NewsCategories.objects.all()
        return context

class DetailView(generic.DetailView):
    model=News
    context_object_name='news'
    template_name= 'homepage/detail_news.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['related_news'] = Newsrelimage.objects.filter(rel_news=self.object)
        return context


class CategoryView(generic.ListView):
    template_name = 'homepage/newscategory_list.html'
    context_object_name = 'categ_news_list'
    paginate_by = 3

    def get_queryset(self,**kwargs):
        return News.objects.filter(category__cname=self.kwargs['categ'])

    def get_context_data(self, **kwargs):
        context=super(CategoryView,self).get_context_data(**kwargs)
        context['categ_news'] = NewsCategories.objects.all()
        return context


class SearchView(View):

    def get(self,request,*args,**kwargs):
        search = request.GET.get('search_field')
        if search:
            queryset = News.objects.filter(title__icontains=search)
            print("----------------- ", queryset.count())
            page = request.GET.get('page', 1)
            print("-------------pageeeeee ", page)
            paginator = Paginator(queryset, 3)
            try:
                news = paginator.page(page)
            except PageNotAnInteger:
                news = paginator.page(1)
            except EmptyPage:
                news = paginator.page(paginator.num_pages)
            return render(request, 'homepage/search_result.html', {'queryset': news,
                                                                   'key': search})
        else:
            form = SearchForm()
            return render(request, 'homepage/search.html', {'form': form})

    def post(self,request,*args,**kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search_field')
            queryset = News.objects.filter(title__icontains=search)
            page = request.GET.get('page', 1)
            paginator = Paginator(queryset, 3)
            try:
                news = paginator.page(page)
            except PageNotAnInteger:
                news = paginator.page(1)
            except EmptyPage:
                news = paginator.page(paginator.num_pages)
            return render(request, 'homepage/search_result.html', {'queryset': news})
        else:
            return render(request, 'homepage/search.html', {'form': form})

class AddNews(View):
    template_name='homepage/addnews.html'
    form_class=NewsForm

    def get(self,request,*args):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args):
        form=self.form_class(request.POST)
        if form.is_valid():
            news=form.save(commit=False)
            news.author=request.user
            news.save()
            return redirect('homepage:news_list')
        else:
            pass
        return render(request,self.template_name,{'form':form})


class AddImages(View):
    template_name='homepage/addimages.html'

    def get(self,request,pk):
        form=NewsImageForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request,pk):
        form=NewsImageForm(request.POST,request.FILES)
        if form.is_valid():
            var=form.save(commit=False)
            newschk=News.objects.get(id=pk)
            var.rel_news=newschk
            var.save()
            return redirect('homepage:newsdetail',pk=newschk.id)
        else:
            pass
        return render(request,self.template_name,{'form':form})


# def subscribeEmailview(request):
#     if request.method == 'POST':
#         form=SubscribeForm(request.POST)
#         if form.is_valid():
#             sub=form.save(commit=False)
#             sub.token=get_random_string(length=32)
#             sub.save()
#             send_mail(
#                 'Subscribe to Newsletter',
#                 """ Hey ( %s ), this email  have been requested to subscribe DailyNews,
#                 Please activate through the below link :  \
#
#                     https://dailynewssayone.herokuapp.com/activate/%s/    \
#                 \
#                     If it was not you please ignore      \
#
#                 From Dailycircle.com
#                 """ % (sub.Email, sub.token),
#                 'dailycirclenews@gmail.com',
#                 [sub.Email],
#
#             )
#             msg="Dear user , Request for subscription is succesful.Inorder to receive newsletter, Kindly activate it from your mail "
#         else:
#             msg="User already subscribed"
#         return render(request,'homepage/subscribesuccess.html',
#                                      {"msg":msg})
#     else:
#         form = SubscribeForm()
#
#     return render(request, 'homepage/subscribe.html', {'form': form})

class SubscribeEmailview(View):
    template_name='homepage/subscribe.html'

    def post(self, request):
        form = SubscribeForm(request.POST)

        if form.is_valid():
            sub = form.save(commit=False)
            sub.token = get_random_string(length=32)
            sub.save()
            send_mail(
                'Subscribe to Newsletter',
                """ Hey ( %s ), this email  have been requested to subscribe DailyNews,
                Please activate through the below link :  \

                    https://dailynewssayone.herokuapp.com/activate/%s/    \
                \
                    If it was not you please ignore      \

                From Dailycircle.com
                """ % (sub.Email, sub.token),
                'dailycirclenews@gmail.com',
                [sub.Email],

            )
            msg = "Dear user , Request for subscription is succesful.Inorder to receive newsletter, Kindly activate it from your mail "
        else:
            msg = "User already subscribed"

        return render(request,self.template_name,{'form':form})


    def get(self,request):
        form=SubscribeForm()
        return render(request, 'homepage/subscribe.html', {'form': form})


def SubscribeActivate(request,token):
    try:
        subobj=Subscribe.objects.get(token=token)
    except(Subscribe.DoesNotExist):
        subobj=None
    if subobj is not None:
        subobj.is_active=True
        subobj.save()
        return render(request,'homepage/subscribesuccess.html',{'msg':'Subscription activated'})
    else:
        return render(request, 'homepage/subscribesuccess.html', {'msg': 'Subscription not succesful'})


class Contactus(View):
    form_class=ContactForm
    template_name='homepage/contactus.html'

    def get(self, request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage:news_list')
        else:
            pass
        return render(request,self.template_name,{'form':form})

