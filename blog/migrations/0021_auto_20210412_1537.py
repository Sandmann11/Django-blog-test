# Generated by Django 3.1.7 on 2021-04-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20210412_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/static/img/lus-200.jpg', upload_to=''),
        ),
    ]