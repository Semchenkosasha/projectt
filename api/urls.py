from .views import get_articles_list, ArticlesList
from django.urls import path

urlpatterns = [
    path('get_articles_list/', get_articles_list),
    path('get_articles_list/', ArticlesList.as_view()),
]