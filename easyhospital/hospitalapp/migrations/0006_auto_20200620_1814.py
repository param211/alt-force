# Generated by Django 3.0.6 on 2020-06-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0005_auto_20200620_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='email',
            field=models.EmailField(default='example@mail.com', max_length=100, unique=True),
        ),
    ]