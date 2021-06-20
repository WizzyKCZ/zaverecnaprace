from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import games

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
    path('', RedirectView.as_view(url='games/')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "DDH Administrace"
admin.site.site_title = "Databáze digitálních her"
admin.site.index_title = "Vítejte v administrační části DDH"

handler404 = 'games.views.error_404'
handler500 = 'games.views.error_500'
handler403 = 'games.views.error_403'
handler400 = 'games.views.error_400'

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
    urlpatterns += [re_path(r'^500/$', games.views.error_500)]
    urlpatterns += [re_path(r'^400/$', games.views.error_400)]
    urlpatterns += [re_path(r'^404/$', games.views.error_404)]
    urlpatterns += [re_path(r'^403/$', games.views.error_403)]
