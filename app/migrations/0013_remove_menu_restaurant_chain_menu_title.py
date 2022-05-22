# Generated by Django 4.0.4 on 2022-05-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_menu_restaurant_chain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='restaurant_chain',
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
    ]