"""newsweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from signup import views as core_views
urlpatterns = [
    url(r'^',include('homepage.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$',auth_views.login,{'template_name':'signup/login.html'},name='login'),
    url(r'^accounts/login/$',auth_views.login,{'template_name':'signup/login.html'},name='login1'),
    url(r'^logout/$',auth_views.logout,{'next_page':'homepage:news_list'},name='logout'),

    url(r'^password_reset/$',auth_views.password_reset,name='password_reset'),
    url(r'^password_reset/done/$',auth_views.password_reset_done,name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,name="password_reset_confirm"),
    url(r'^reset/done/$',auth_views.password_reset_complete,name='password_reset_complete'),

    url(r'^password/$',core_views.change_password,name='change_password'),

    url(r'^oauth/', include('social_django.urls',namespace='social')),

    url(r'^comments/', include('django_comments.urls')),
]