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


class Menu(models.Model):
    price = models.IntegerField


class RestaurantChain(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    owners_name = models.CharField(max_length=50, verbose_name="Имя владельца")
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE, )


class Restaurant(models.Model):
    address = models.CharField(max_length=50, verbose_name="Адресс")
