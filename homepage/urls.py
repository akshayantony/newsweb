from django.conf.urls import url
from django.conf.urls.static import static
from newsweb import settings
from . import views

app_name='homepage'
urlpatterns=[
    url(r'^dailycircle/$',views.NewsView.as_view(),name="news_list"),
    url(r'^dailycircle/(?P<username>[\w]+)/$',views.NewsView.as_view(),name="news_list1"),
    url(r'^dailycircle/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='newsdetail'),
    url(r'^dailycircle/(?P<categ>[A-Z][a-z]+)/$',views.CategoryView.as_view(),name='categorylist'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)