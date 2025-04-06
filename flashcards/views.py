# ------------------------------------------------------------------------------------------------------------
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# ------------------------------------------------------------------------------------------------------------
from .models import Flashcard, Category
from .forms import FlashcardForm, CategoryForm, RegisterForm
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
@login_required
def by_user_flashcards(request):
    flashcards = Flashcard.objects.filter(category__user=request.user)
    categories = Category.objects.filter(user=request.user)
    return render(request, 'flashcards/index.html',  { 'flashcards' : flashcards, 'categories': categories})
# ------------------------------------------------------------------------------------------------------------
def other_page(request, page):
    try:
        template = get_template('flashcards/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
# ------------------------------------------------------------------------------------------------------------
def by_category(request, category_id):
    flashcards = Flashcard.objects.filter(category = category_id)
    categories = Category.objects.filter(user=request.user)
    current_category = Category.objects.get(pk = category_id)

    context = {
        'flashcards': flashcards,
        'categories': categories,
        'current_category': current_category,
    }
    return render(request, 'flashcards/by_category.html', context)
# ------------------------------------------------------------------------------------------------------------
@login_required
def profile(request):
    return render(request, 'flashcards/profile.html')
# ------------------------------------------------------------------------------------------------------------
def ajax_flashcards(request):
    flashcards = Flashcard.objects.filter(category__user=request.user)

    flashcards_data = []
    for flashcard in flashcards:
        flashcards_data.append({
            'word': flashcard.word,
            'translate': flashcard.translate,
            'example': flashcard.example,
            'tip': flashcard.tip,
        })
    return JsonResponse({'flashcards': flashcards_data})
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
# ------------------------------------------------------------------------------------------------------------    
class CategoryCreateView(CreateView):
    template_name = 'flashcards/create_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
# ------------------------------------------------------------------------------------------------------------    
class FlashcardLoginView(LoginView):
    template_name = 'flashcards/login.html'
# ------------------------------------------------------------------------------------------------------------ 
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'flashcards/register.html'
    success_url = '/'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
# ------------------------------------------------------------------------------------------------------------