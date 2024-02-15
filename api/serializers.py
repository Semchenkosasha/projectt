from .models import Article, ImageArticle
from rest_framework import serializers


class ImageArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageArticle
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    images = ImageArticleSerializer(many=True)
    class Meta:
        model = Article
        fields = ['id', 'link', 'head_title', 'keywords', 'description', 'title', 'preview_img', 'subtitle', 'photo_text', 'mark_up', 'images']