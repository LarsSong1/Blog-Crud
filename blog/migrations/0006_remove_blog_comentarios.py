# Generated by Django 4.1.7 on 2023-02-25 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_fechapublicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comentarios',
        ),
    ]