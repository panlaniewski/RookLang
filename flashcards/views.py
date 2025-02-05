from django.shortcuts import render

from .models import Flashcard, Category

def index(request):
    flshcards = Flashcard.objects.all()
    categories = Category.objects.all()
    return render(request, 'flashcards/index.html', { 'flshcards' : flshcards, 'categories': categories})

def by_category(request, category_id):
    flshcards = Flashcard.objects.filter(category = category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk = category_id)
    context = {
        'flshcards': flshcards,
        'categories': categories,
        'current_category': current_category,
    }
    return render(request, 'flashcards/by_category.html', context)

    
