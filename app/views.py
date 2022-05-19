from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish, DishType


# Create your views here.
def index(request):
    q = request.GET.get('q')
    dishes = Dish.objects.filter(dish_type__title=q)
    dish_types = DishType.objects.all()
    # dishes = Dish.objects.all()
    # .order_by('id')
    context = {'title': 'Главная', 'dishes': dishes, 'dish_types': dish_types}
    return render(request, 'app/index.html', context)


def about(request):
    return render(request, 'app/about.html')
