# Generated by Django 3.2.13 on 2022-06-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_redesociales_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temasimportantes',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
