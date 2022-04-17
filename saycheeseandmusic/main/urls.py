from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('audiolibrary', views.audio_library, name='audiolibrary'),
    path('developers_info', views.developers_info, name='developers'),
    path('suicide_boys_page', views.suicide_boys_page, name='suicide_boys_page'),
    path('suicide_boys_discography', views.suicide_boys_discography, name='suicide_boys_discography'),
]
