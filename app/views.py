from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish, DishType
from django.db.models import Q


# Create your views here.
def index(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    dishes = Dish.objects.filter(
        Q(dish_type__title__icontains=q) |
        Q(title__icontains=q)
    )
    dish_types = DishType.objects.all()
    # dishes = Dish.objects.all()
    # .order_by('id')
    object_type_for_search = 'dish'
    context = {'title': 'Главная', 'dishes': dishes, 'dish_types': dish_types,
               'object_type_for_search': object_type_for_search}
    return render(request, 'app/index.html', context)


def about(request):
    return render(request, 'app/about.html')
