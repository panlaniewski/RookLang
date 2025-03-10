from django.urls import path
from .views import other_page
from .views import index, by_category, FlashcardCreateView, CategoryCreateView

urlpatterns = [
    path('add_category/', CategoryCreateView.as_view(), name = 'add_category'),
    path('add_flashcard/', FlashcardCreateView.as_view(), name = 'add_flashcard'),
    path('<int:category_id>/', by_category, name = 'by_category'),
    path('<str:page>/', other_page, name = 'other'),
    path('', index, name = 'index'),
]
