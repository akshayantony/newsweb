from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from signup import views as core_views
from newsweb.sitemaps import TodoSitemap
from django.contrib.sitemaps.views import sitemap
sitemaps={
    'todos':TodoSitemap()
}

urlpatterns = [
    url(r'^',include('homepage.urls'),name='homepage'),
    url(r'^admin/', admin.site.urls),

    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$',auth_views.login,{'template_name':'signup/login.html'},name='login'),
    url(r'^accounts/login/$',auth_views.login,{'template_name':'signup/login.html'},name='login1'),
    url(r'^logout/$',auth_views.logout,{'next_page':'homepage:news_list'},name='logout'),

    url(r'^password_reset/$',auth_views.password_reset,{'template_name':'signup/pssword_reset_form.html'},name='password_reset'),
    url(r'^password_reset/done/$',auth_views.password_reset_done,{'template_name':'signup/pssword_reset_done.html'},name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,{'template_name':'signup/pssword_reset_confirm.html'},name="password_reset_confirm"),
    url(r'^reset/done/$',auth_views.password_reset_complete,{'template_name':'signup/pssword_reset_complete.html'},name='password_reset_complete'),

    url(r'^password/$',core_views.change_password,name='change_password'),

    url(r'^comments/', include('django_comments.urls')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^sitemaps.xml',sitemap, {'sitemaps': sitemaps}),
    url(r'^robots.txt', include('robots.urls')),
]