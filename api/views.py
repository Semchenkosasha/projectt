from rest_framework.generics import ListAPIView
from .models import Article
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer


# Create your views here.

@api_view(['GET'])
def get_articles_list(request):
    articles_queryset = Article.objects.all()
    print(articles_queryset)
    serializer = ArticleSerializer(articles_queryset, many=True)
    return Response(serializer.data)

class ArticlesList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer