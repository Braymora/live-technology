# Generated by Django 5.0.2 on 2024-05-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0004_alter_cursos_imagenes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='imagenes',
        ),
        migrations.AddField(
            model_name='cursos',
            name='curso',
            field=models.TextField(default='hola'),
        ),
    ]
