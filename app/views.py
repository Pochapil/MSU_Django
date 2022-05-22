from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish, DishType, Menu, MenuItem
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def about(request):
    return render(request, 'app/about.html')


def menu(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    menu_list = MenuItem.objects.filter(
        Q(dish__dish_type__title__icontains=q) |
        Q(dish__title__icontains=q)
    )
    dish_types = DishType.objects.all()
    # dishes = Dish.objects.all()
    # .order_by('id')
    object_type_for_search = 'dish'
    context = {'title': 'Меню', 'menu_list': menu_list, 'dish_types': dish_types,
               'object_type_for_search': object_type_for_search}

    return render(request, 'app/menu.html', context)


def restaurant(request):
    return render(request, 'app/restaurant.html')


def dish(request):
    dish_title = request.GET.get('name')
    dish = Dish.objects.get(title__exact=dish_title)
    context = {'title': dish_title, 'dish': dish}
    return render(request, 'app/dish.html', context)
