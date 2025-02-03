from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('flashcards/', include('flashcards.urls')),
    path('admin/', admin.site.urls),
]
