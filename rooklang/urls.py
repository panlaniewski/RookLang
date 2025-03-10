from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('', include('flashcards.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))

