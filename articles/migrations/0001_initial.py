# Generated by Django 3.0.5 on 2020-04-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(default='', max_length=500, verbose_name='description')),
                ('image_url', models.URLField(null=True)),
            ],
        ),
    ]
