from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    text = models.CharField(max_length=100, verbose_name="Текст")
    publishing_date = models.DateTimeField(verbose_name="дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Новость"
        verbose_name_plural = u"Новости"


class RestaurantChain(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название Сети")
    menu = models.OneToOneField('Menu', verbose_name="Меню", on_delete=models.CASCADE)
    owners_name = models.CharField(max_length=50, verbose_name="Имя владельца")


class Restaurant(models.Model):
    restaurant_chain = models.ForeignKey(RestaurantChain, verbose_name="Сеть ресторанов", on_delete=models.CASCADE)
    address = models.CharField(max_length=50, verbose_name="Адрес")
    manager_name = models.CharField(max_length=50, verbose_name="Имя менеджера")


class Menu(models.Model):
    dish = models.ManyToManyField('Dish', verbose_name="Блюдо")
    serving_size = models.CharField(max_length=50, verbose_name="Размер порции")
    price = models.IntegerField(verbose_name="Цена")


class Dish(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название блюда")
    dish_type = models.ForeignKey('DishTypes', verbose_name="Тип блюда", on_delete=models.CASCADE)
    description = models.CharField(max_length=50, verbose_name="Описание блюда")


class DishTypes(models.Model):
    dish_type = models.CharField(max_length=50, verbose_name="Тип блюда")
