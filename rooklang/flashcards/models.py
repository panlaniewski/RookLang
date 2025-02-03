from django.db import models

class Flashcard(models.Model):
    word = models.CharField(max_length = 50)
    translate = models.CharField(max_length = 50)
    example = models.TextField(null = True, blank = True)
    tip = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.word

    class Meta :
        verbose_name_plural = 'Слова'
        verbose_name = 'Слово'
        ordering = ['id']
