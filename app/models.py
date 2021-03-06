from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class RestaurantChain(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    menu = models.OneToOneField('Menu', verbose_name="Меню", on_delete=models.SET_NULL, null=True)
    customer_satisfaction_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
                                                    verbose_name="Оценка клиентов")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Сеть ресторанов"
        verbose_name_plural = u"Сети ресторанов"


class Restaurant(models.Model):
    restaurant_chain = models.ForeignKey(RestaurantChain, verbose_name="Название сети ресторанов",
                                         on_delete=models.CASCADE)
    address = models.CharField(max_length=50, verbose_name="Адрес")
    phone_number = models.OneToOneField('PhoneNumber', verbose_name="Номер телефона", on_delete=models.SET_NULL,
                                        null=True)

    def __str__(self):
        return self.restaurant_chain.title + " на " + self.address

    class Meta:
        verbose_name = u"Ресторан"
        verbose_name_plural = u"Список ресторанов"


class Menu(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    menu_list = models.ManyToManyField('MenuItem', verbose_name="Меню")

    def __str__(self):
        return "Меню ресторана " + self.title

    class Meta:
        verbose_name = u"Меню"
        verbose_name_plural = u"Список меню"


class MenuItem(models.Model):
    dish = models.OneToOneField('Dish', verbose_name="Блюдо", on_delete=models.CASCADE)
    serving_size = models.CharField(max_length=50, verbose_name="Размер порции")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.dish.title + " " + str(self.price)

    class Meta:
        verbose_name = u"Позиция в меню"
        verbose_name_plural = u"Позиции меню"


class Dish(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название блюда")
    dish_type = models.ForeignKey('DishType', verbose_name="Тип блюда", on_delete=models.SET_NULL, null=True)
    description = models.TextField(verbose_name="Описание блюда", null=True)
    ingredient_list = models.ManyToManyField('Ingredient', verbose_name="Список ингредиентов")

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


class Ingredient(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название ингредиента")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Ингредиент"
        verbose_name_plural = u"Ингредиенты"


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=50, verbose_name="Номер телефона")

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = u"Номер телефона"
        verbose_name_plural = u"Номера телефонов"
