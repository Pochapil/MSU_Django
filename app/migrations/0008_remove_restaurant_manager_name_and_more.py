# Generated by Django 4.0.4 on 2022-05-21 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_dish_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='manager_name',
        ),
        migrations.RemoveField(
            model_name='restaurantchain',
            name='owners_name',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(default=7919, max_length=50, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_chain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.restaurantchain', verbose_name='Название сети ресторанов'),
        ),
        migrations.AlterField(
            model_name='restaurantchain',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
