from django.conf.urls import url,include
from django.conf.urls.static import static
from newsweb import settings
from . import views
from django.views.generic import TemplateView

app_name='homepage'
urlpatterns=[
    url(r'^dailycircle/search/$', views.SearchView.as_view(), name='search'),
    url(r'^dailycircle/addnews/$', views.AddNews.as_view(), name='addnews'),
    url(r'^dailycircle/addimages/(?P<pk>[0-9]+)$', views.AddImages.as_view(), name='addnewsimages'),
    url(r'^dailycircle/subscribe/$', views.SubscribeEmailview.as_view(), name='subscribe'),
    url(r'^dailycircle/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='newsdetail'),
    url(r'^dailycircle/(?P<categ>[^\n]+)/$',views.CategoryView.as_view(),name='categorylist'),
    url(r'^$',views.NewsView.as_view(),name="news_list"),
    url(r'^activate/(?P<token>[0-9a-zA-Z]{32})/$', views.SubscribeActivate, name='activate'),
    url(r'^contactus/$',views.Contactus.as_view(),name="contactus"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)