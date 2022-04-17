from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Song

def home(request):
    return render(request, 'main/home.html')


def audio_library(request):
    return render(request, 'main/audiolibrary.html')


def developers_info(request):
    return render(request,"main/libmenutest.html")


def suicide_boys_page(request):
    paginator = Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj": page_obj}
    return render(request, 'main/test.html', context)
