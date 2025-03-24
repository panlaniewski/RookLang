from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Flashcard, Category

class FlashcardForm(ModelForm):
    class Meta:
        model = Flashcard
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)