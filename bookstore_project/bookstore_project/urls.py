from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # media
from django.conf.urls.static import static  # media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('users.urls')),
    path('accounts', include('allauth.urls')),
    path('books/', include('books.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
