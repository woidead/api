# Generated by Django 4.1.2 on 2022-10-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='students name')),
                ('last_name', models.CharField(max_length=20, verbose_name='stidents last name')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20, verbose_name='sex')),
                ('departament', models.CharField(max_length=20, verbose_name='departament')),
            ],
        ),
    ]
