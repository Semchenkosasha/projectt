from django.contrib import admin
from django.db import models

# Create your models here.

class Article(models.Model):
    link = models.TextField('Ссылка на новость')
    head_title = models.CharField('Head заголовок',max_length=500)
    keywords = models.TextField('Ключевые слова')
    description = models.TextField('Описание')
    title = models.CharField('Заголовок',max_length=500)
    preview_img = models.ImageField('Главное изображение',upload_to='articles_images')
    subtitle = models.CharField('Подзаголовок',max_length=500)
    photo_text = models.TextField('Текст на фотографии')
    mark_up = models.TextField()
    is_published = models.BooleanField('Опубликовано',default=False)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticleAdmin(admin.ModelAdmin):
    list_editable = ['is_published']
    list_display = ['title', 'is_published']
    list_filter = ['is_published']

class ImageArticle(models.Model):
    image = models.ImageField('Изображение',upload_to='articles_images')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='images', verbose_name='Статья')
    def __str__(self):
        return f'{self.article}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'