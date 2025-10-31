from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','name','date']   # Read operation

admin.site.register(Article , ArticleAdmin)

