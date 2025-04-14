from django import forms
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
        exclude = ['user']

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class SearchForm(ModelForm):
    keyword = forms.CharField(required=False, max_length=20, label='')