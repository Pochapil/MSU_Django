# Generated by Django 4.0.4 on 2022-05-22 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_menu_dish_remove_menu_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='dish',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.dish', verbose_name='Блюдо'),
        ),
    ]