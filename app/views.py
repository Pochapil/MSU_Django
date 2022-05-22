from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish, DishType, Menu, MenuItem, Restaurant
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
    ).order_by('dish__dish_type', 'dish__title')
    dish_types = DishType.objects.all()
    # dishes = Dish.objects.all()
    # .order_by('id')
    object_type_for_search = 'блюдо'
    context = {'title': 'Меню', 'menu_list': menu_list, 'dish_types': dish_types,
               'object_type_for_search': object_type_for_search}

    return render(request, 'app/menu.html', context)


def restaurant_list(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    restaurant_list = Restaurant.objects.filter(address__icontains=q).order_by('address')
    object_type_for_search = 'ресторан'
    context = {'title': 'Список ресторанов', 'restaurant_list': restaurant_list,
               'object_type_for_search': object_type_for_search}

    return render(request, 'app/restaurant_list.html', context)


def dish(request):
    dish_id = request.GET.get('id')
    dish = Dish.objects.get(pk__exact=dish_id)
    dish_title = dish.title
    context = {'title': dish_title, 'dish': dish}
    return render(request, 'app/dish.html', context)


def restaurant(request):
    restaurant_id = request.GET.get('id')
    restaurant = Restaurant.objects.get(pk__exact=restaurant_id)
    title = restaurant.restaurant_chain.title
    context = {'title': title, 'restaurant': restaurant}
    return render(request, 'app/restaurant.html', context)
