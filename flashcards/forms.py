from django.forms import ModelForm
from .models import Flashcard, Category

class FlashcardForm(ModelForm):
    class Meta:
        model = Flashcard
        fields = ('word', 'translate', 'example', 'tip', 'category')

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)