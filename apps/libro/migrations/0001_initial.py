# Generated by Django 3.1.3 on 2020-11-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]