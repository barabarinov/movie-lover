from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from crew.views import DirectorDetailView

urlpatterns = [
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
    path('crew/', include('crew.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
