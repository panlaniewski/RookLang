from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', by_user_flashcards, name = 'index'),
    path('get_data/', ajax_flashcards, name='get_data'),
    path('<int:category_id>/', by_category, name = 'by_category'),
    path('flashcard/<int:pk>/delete/', delete_flashcard, name='delete_flashcard'),
    path('category/<int:pk>/delete/', delete_category, name='delete_category'),
    path('add_flashcards/', FlashcardCreateView.as_view(), name = 'add_flashcard'),
    path('add_category/', CategoryCreateView.as_view(), name = 'add_category'),
    path('<str:page>/', other_page, name = 'other'),
    path('accounts/login/', FlashcardLoginView.as_view(), name = 'login'),
    path('accounts/profile/', profile, name = 'profile'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name = 'logout'),
    path('accounts/register/', RegisterView.as_view(), name = 'register'),
]
