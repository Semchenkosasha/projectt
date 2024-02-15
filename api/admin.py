from api.models import Article, ImageArticle, ArticleAdmin
from django.contrib import admin

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ImageArticle)
