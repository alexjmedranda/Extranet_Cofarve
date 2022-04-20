# Generated by Django 4.0.4 on 2022-04-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('passwd', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imageX', models.FileField(blank=True, max_length=254, upload_to='public/static/')),
            ],
        ),
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=300)),
                ('state', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('enlace', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='RedeSociales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state', models.BooleanField()),
                ('enlace', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TemasImportantes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('enlace', models.CharField(max_length=300)),
            ],
        ),
    ]
