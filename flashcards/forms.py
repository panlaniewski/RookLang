from django.forms import ModelForm
from .models import Flashcard

class FlashcardForm(ModelForm):
    class Meta:
        model = Flashcard
        fields = ('word', 'translate', 'example', 'tip', 'category')