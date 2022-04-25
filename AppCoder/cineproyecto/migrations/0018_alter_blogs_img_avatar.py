# Generated by Django 4.0.3 on 2022-04-24 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cineproyecto', '0017_blogs_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='Imagen'),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='Avatar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]