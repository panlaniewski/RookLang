from django.urls import path

from .views import index, by_category, FlashcardCreateView

urlpatterns = [
    path('add/', FlashcardCreateView.as_view(), name = 'add'),
    path('<int:category_id>/', by_category, name = 'by_category'),
    path('', index, name = 'index'),
]