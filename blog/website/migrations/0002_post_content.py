# Generated by Django 3.1.7 on 2021-02-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='Vazio'),
        ),
    ]
