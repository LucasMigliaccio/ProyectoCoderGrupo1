# Generated by Django 4.0.3 on 2022-04-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineproyecto', '0008_alter_movies_options_alter_movies_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='body',
            field=models.TextField(max_length=300, verbose_name='Contenido'),
        ),
    ]