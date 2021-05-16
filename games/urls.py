from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hry/', views.HraListView, name='hry'),
    path('hry/<int:pk>/', views.HraDetailView.as_view(), name='hra_detail')
]