from django.shortcuts import render

from .models import Flashcard

def index(request):
    flshcards = Flashcard.objects.all()
    return render(request, 'flashcards/index.html', { 'flshcards' : flshcards})
