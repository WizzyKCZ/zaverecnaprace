from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hry/', views.HraListView, name='hry'),
    path('hry/<int:pk>/', views.HraDetailView.as_view(), name='hra_detail'),
    path('hry/create/', views.HraCreate.as_view(), name='hra-create'),
    path('hry/<int:pk>/update/', views.HraUpdate.as_view(), name='hra-update'),
    path('hry/<int:pk>/delete/', views.HraDelete.as_view(), name='hra-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('hry/<int:pk>/edit/', views.edit_hra, name='hra-edit'),
]