from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class RestaurantChain(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название Сети")
    menu = models.OneToOneField('Menu', verbose_name="Меню", on_delete=models.SET_NULL, null=True)
    customer_satisfaction_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
                                                    verbose_name="Оценка клиентов")
    owners_name = models.CharField(max_length=50, verbose_name="Имя владельца")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Сеть ресторанов"
        verbose_name_plural = u"Сети ресторанов"


class Restaurant(models.Model):
    restaurant_chain = models.ForeignKey(RestaurantChain, verbose_name="Сеть ресторанов", on_delete=models.CASCADE)
    address = models.CharField(max_length=50, verbose_name="Адрес")
    manager_name = models.CharField(max_length=50, verbose_name="Имя менеджера")

    def __str__(self):
        return self.restaurant_chain.title

    class Meta:
        verbose_name = u"Ресторан"
        verbose_name_plural = u"Список ресторанов"


class Menu(models.Model):
    dish = models.ManyToManyField('Dish', verbose_name="Блюдо")
    serving_size = models.CharField(max_length=50, verbose_name="Размер порции")
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = u"Меню"
        verbose_name_plural = u"Список меню"


class Dish(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название блюда")
    dish_type = models.ForeignKey('DishType', verbose_name="Тип блюда", on_delete=models.SET_NULL, null=True)
    description = models.TextField(verbose_name="Описание блюда")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Блюдо"
        verbose_name_plural = u"Список Блюд"


class DishType(models.Model):
    title = models.CharField(max_length=50, verbose_name="Тип блюда")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Тип блюда"
        verbose_name_plural = u"Типы блюд"
