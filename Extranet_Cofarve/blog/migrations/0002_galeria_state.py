# Generated by Django 4.0.4 on 2022-06-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
