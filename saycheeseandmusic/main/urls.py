from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('audiolibrary', views.audio_library, name='audiolibrary'),
    path('developers_info', views.developers_info, name='developers'),
]
