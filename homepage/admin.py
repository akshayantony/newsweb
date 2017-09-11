from django.contrib import admin
from .models import News, NewsCategories,Newsrelimage,Subscribe,Contactus

class NewsrelimageInline(admin.TabularInline):
    model = Newsrelimage
    extra = 3

class NewsAdmin(admin.ModelAdmin):
    inlines = [ NewsrelimageInline, ]


admin.site.register(News)
admin.site.register(NewsCategories)
admin.site.register(Newsrelimage)
admin.site.register(Subscribe)
admin.site.register(Contactus)