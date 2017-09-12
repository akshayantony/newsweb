from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
from homepage.models import News,NewsCategories,Newsrelimage,Subscribe,Contactus
from homepage.forms import SearchForm,NewsForm ,NewsImageForm,SubscribeForm,ContactForm #,CategoriesForm
from homepage.models import Subscribe
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.views.generic.edit import FormView


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
        # print("-context is**********", context['related_news'])
        return context


class CategoryView(generic.ListView):
    template_name = 'homepage/newscategory_list.html'
    context_object_name = 'categ_news_list'
    paginate_by = 3

    def get_queryset(self,**kwargs):
        return News.objects.filter(category__cname=self.kwargs['categ'])


def search(request):
    if(request.method == 'POST'):
        form=SearchForm(request.POST)

        if form.is_valid():
            search=form.cleaned_data.get('search_field')
            queryset=News.objects.filter(title__icontains=search)
            return render(request,'homepage/search_result.html',{'queryset':queryset})

    else:
        form=SearchForm()

    return render(request,'homepage/search.html',{'form':form})

def addNews(request):
    if (request.method == 'POST'):
        form=NewsForm(request.POST)
        #sub_form=NewsImageForm(request.POST,prefix="category")

        if form.is_valid():
            news=form.save(commit=False)
            news.author = request.user
            #sub_form.save()
            news.save()
            return redirect('homepage:news_list')

    else:
        form = NewsForm()
        #sub_form = NewsImageForm(prefix="category")

    return render(request,'homepage/addnews.html',{'form':form})#,'sub_form':sub_form})

def addimages(request,pk):
    if request.method == 'POST':
        form=NewsImageForm(request.POST,request.FILES)
        if form.is_valid():
            var=form.save(commit=False)
            newschk=News.objects.get(id=pk)
            var.rel_news=newschk
            var.save()
            return redirect('homepage:newsdetail',pk=newschk.id)

    else:
        form = NewsImageForm()
        #sub_form = NewsImageForm(prefix="category")

    return render(request,'homepage/addimages.html',{'form':form})#,'sub_form':sub_form})


def subscribeEmailview(request):
    if request.method == 'POST':
        print("111111111111111111")
        print(request.POST.get('Email'))
        form=SubscribeForm(request.POST)
        print(form)
        if form.is_valid():
            sub=form.save(commit=False)
            sub.token=get_random_string(length=32)
            sub.save()
            send_mail(
                'Subscribe to Newsletter',
                """ Hey ( %s ), this email  have been requested to subscribe DailyNews, 
                Please activate through the below link :  \

                    http://127.0.0.1:8000/activate/%s/    \
                \
                    If it was not you please ignore      \

                From Dailycircle.com
                """ % (sub.Email, sub.token),
                'dailycirclenews@gmail.com',
                [sub.Email],

            )
            msg="Subscription succesful"
        else:
            msg="invalid form"
        return render(request,'homepage/subscribesuccess.html',
                                     {"msg":msg})

    else:
        form = SubscribeForm()

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


def Contactus(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
        return redirect('homepage:news_list')
    else:
        form = ContactForm()
    return render(request, 'homepage/contactus.html', {'form': form})



    # model_form=ContactForm
    # model=Contactus
    # template_name="homepage/contactus.html"
    # success_url="homepage:news_list"
    #
    # def form_invalid(self,form):
    #     return render(self.request,self.template_name,{'form':self.model_form(form)})
    #
    # def post(self,request):
    #     form=self.model_form(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         pass
    #     return render(request,self.template_name,{'form':self.model_form()})
    #
    #     def get(self,request):
    #         return render(request,self.template_name,{'form':self.model_form()})


# class UploadView(FormView):
#     template_name = 'homepage/addnews.html'
#     form_class = AddForm
#     success_url = 'homepage:news_list'
#
#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         instance.author = self.request.user
#         instance.save()
#
#         return super(UploadView, self).form_valid(form)
