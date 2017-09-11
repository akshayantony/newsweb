from django.conf.urls import url,include
from django.conf.urls.static import static
from newsweb import settings
from . import views
from django.views.generic import TemplateView

app_name='homepage'
urlpatterns=[
    url(r'^dailycircle/$',views.NewsView.as_view(),name="news_list"),
    url(r'^dailycircle/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='newsdetail'),
    url(r'^dailycircle/(?P<categ>[A-Z][a-z]+)/$',views.CategoryView.as_view(),name='categorylist'),
    url(r'^dailycircle/search/$',views.search,name = 'search'),
    url(r'^dailycircle/addnews/$',views.addNews,name='addnews'),
    url(r'^dailycircle/addimages/(?P<pk>[0-9]+)$',views.addimages,name='addnewsimages'),
    url(r'^dailycircle/subscribe/$',views.subscribeEmailview,name='subscribe'),
    url(r'^activate/(?P<token>[0-9a-zA-Z]{32})/$',views.SubscribeActivate,name='activate'),
    url(r'^contactus/$',views.Contactus,name="contactus"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)