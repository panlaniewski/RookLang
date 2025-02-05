from django.db import models
# ---------------------------------------------------------

class Flashcard(models.Model):
    word = models.CharField(max_length = 50, verbose_name = 'Слово')
    translate = models.CharField(max_length = 50, verbose_name = 'Перевод')
    example = models.TextField(null = True, blank = True, verbose_name = 'Пример употребления')
    tip = models.TextField(null = True, blank = True, verbose_name = 'Подсказка')
    category = models.ForeignKey('Category', null = True, on_delete = models.PROTECT, verbose_name = 'Тема')

    def __str__(self):
        return self.word

    class Meta :
        verbose_name_plural = 'Слова'
        verbose_name = 'Слово'
        ordering = ['id']

# ---------------------------------------------------------

class Category(models.Model):
    name = models.CharField(max_length = 20, db_index = True, verbose_name = "Название")

    def __str__(self):
        return self.name

    class Meta :
        verbose_name_plural = 'Темы'
        verbose_name = 'Тема'
        ordering = ['name']

# ---------------------------------------------------------

class Language(models.Model):
    name = models.CharField(max_length = 30)
    alphabet = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    class Meta :
        verbose_name_plural = 'Языки'
        verbose_name = 'Язык'
        ordering = ['id']