# Generated by Django 3.2.4 on 2021-06-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='public/')),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
