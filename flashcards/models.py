from django.db import models
from django.contrib.auth.models import User
from .utilities import get_timestamp_path
# -----------------------------------------------------------------------------------------
class Flashcard(models.Model):
    category = models.ForeignKey('Category', null = True, on_delete = models.CASCADE, verbose_name = 'Тема')
    word = models.CharField(max_length = 50, verbose_name = 'Слово')
    translate = models.CharField(max_length = 50, verbose_name = 'Перевод')
    example = models.TextField(null = True, blank = True, verbose_name = 'Пример употребления')
    tip = models.TextField(null = True, blank = True, verbose_name = 'Подсказка')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')

    def __str__(self):
        return self.word
    
    class Meta :
        verbose_name_plural = 'Слова'
        verbose_name = 'Слово'
        ordering = ['id']

# -----------------------------------------------------------------------------------------
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20, db_index = True, verbose_name = "Название")

    def __str__(self):
        return self.name

    class Meta :
        verbose_name_plural = 'Темы'
        verbose_name = 'Тема'
        ordering = ['name']
# -----------------------------------------------------------------------------------------