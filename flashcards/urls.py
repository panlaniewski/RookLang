from django.urls import path

from .views import index

urlpatterns = [
    # path('<int:category_id>/', by_category)
    path('', index)
]