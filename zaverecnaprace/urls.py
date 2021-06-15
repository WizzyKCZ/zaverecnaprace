from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
    path('', RedirectView.as_view(url='games/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "DDH Administrace"
admin.site.site_title = "Databáze digitálních her"
admin.site.index_title = "Vítejte v administrační části DDH"