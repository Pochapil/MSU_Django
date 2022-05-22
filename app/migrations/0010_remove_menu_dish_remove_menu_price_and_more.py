# Generated by Django 4.0.4 on 2022-05-22 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_phonenumber_alter_restaurant_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='price',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='serving_size',
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serving_size', models.CharField(max_length=50, verbose_name='Размер порции')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dish', verbose_name='Блюдо')),
            ],
            options={
                'verbose_name': 'Позиция в меню',
                'verbose_name_plural': 'Позиции меню',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_list',
            field=models.ManyToManyField(to='app.menuitem', verbose_name='Меню'),
        ),
    ]
