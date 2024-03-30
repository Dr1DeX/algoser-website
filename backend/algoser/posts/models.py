from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=254, verbose_name='Название категории')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Posts(models.Model):
    title = models.CharField(max_length=254, verbose_name='Заголовок статьи')
    text = models.TextField(verbose_name='Описание статьи')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='category',
                                 verbose_name='Категория')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'Автор: {self.author}; Заголовок: {self.title}'

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
