# ------------------------------------------------------------------------------------------------------------
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# ------------------------------------------------------------------------------------------------------------
from .models import Flashcard, Category
from .forms import FlashcardForm, CategoryForm
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
def index(request):
    flashcards = Flashcard.objects.all()
    categories = Category.objects.all()
    return render(request, 'flashcards/index.html', { 'flashcards' : flashcards, 'categories': categories} )

def other_page(request, page):
    try:
        template = get_template('flashcards/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

def by_category(request, category_id):
    flashcards = Flashcard.objects.filter(category = category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk = category_id)
    context = {
        'flashcards': flashcards,
        'categories': categories,
        'current_category': current_category,
    }
    return render(request, 'flashcards/by_category.html', context)
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
class FlashcardCreateView(CreateView):
    template_name = 'flashcards/create_flashcard.html'
    form_class = FlashcardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
    
class CategoryCreateView(CreateView):
    template_name = 'flashcards/create_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context



    
