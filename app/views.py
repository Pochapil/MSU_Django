from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def year_archive(request, year):  # articles/<int:year>/
    return HttpResponse("Hello, it's year!")


def month_archive(request, year, month):  # articles/<int:year>/<int:month>/
    return HttpResponse("Hello, it's month!")


def article_detail(request, year, month, slug):  # articles/<int:year>/<int:month>/<slug:slug>/
    return HttpResponse("Hello, it's details!")


def index(request):  # /path
    return HttpResponse("Hello, world. It’s index")


def index(request):
    return render(request, 'app/index.html')
