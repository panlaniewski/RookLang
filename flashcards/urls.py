from django.urls import path

from .views import index, by_category

urlpatterns = [
    path('<int:category_id>/', by_category),
    path('', index)
]