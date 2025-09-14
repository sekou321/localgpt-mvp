from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contribute/', views.contribute, name='contribute'),
    path('info/<int:info_id>/', views.info_detail, name='info_detail'),
    path('all_infos/', views.all_infos, name='all_infos'),  # <-- ajouter cette ligne
]
