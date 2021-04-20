# Generated by Django 3.1.7 on 2021-04-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_auto_20210419_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]