from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def audio_library(request):
    return render(request, 'main/audiolibrary.html')


def developers_info(request):
    return render(request, 'main/developers.html')
