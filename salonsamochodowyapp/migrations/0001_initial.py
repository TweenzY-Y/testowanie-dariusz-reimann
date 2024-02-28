# Generated by Django 5.0.2 on 2024-02-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carName', models.CharField(max_length=255)),
                ('carDescription', models.TextField(default='')),
                ('carPrice', models.PositiveSmallIntegerField(default=1)),
                ('carYear', models.PositiveSmallIntegerField(default=2000)),
                ('carImage', models.ImageField(blank=True, null=True, upload_to='media_car')),
            ],
        ),
    ]