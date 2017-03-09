from django.contrib import admin
from model_one.models import *
# Register your models here.

#@admin.register(Publisher) 用装饰器方法来让admin显示更多内容
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','country','state_province','city')
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)
admin.site.register(Publisher,PublisherAdmin)