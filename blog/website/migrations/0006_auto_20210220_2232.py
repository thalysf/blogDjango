# Generated by Django 3.1.7 on 2021-02-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_post_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
        migrations.AddField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
