from django.urls import path
from .views import index, by_category, other_page, FlashcardLoginView, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name = 'index'),
    path('<int:category_id>/', by_category, name = 'by_category'),
    path('<str:page>/', other_page, name = 'other'),
    path('accounts/login/', FlashcardLoginView.as_view(), name = 'login'),
    path('accounts/profile/', profile, name = 'profile'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name = 'logout'),
]
