# Generated by Django 4.1.3 on 2022-11-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_house_img1_alter_house_img2_alter_house_img3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='img1',
            field=models.ImageField(upload_to='static/upload'),
        ),
        migrations.AlterField(
            model_name='house',
            name='img2',
            field=models.ImageField(upload_to='static/upload'),
        ),
        migrations.AlterField(
            model_name='house',
            name='img3',
            field=models.ImageField(upload_to='static/upload'),
        ),
    ]
