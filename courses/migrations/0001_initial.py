# Generated by Django 2.2.6 on 2019-10-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('educator', models.CharField(max_length=100)),
                ('excerpt', models.TextField(max_length=300)),
                ('description', models.TextField()),
                ('num_lessons', models.PositiveSmallIntegerField(default=0)),
                ('picture', models.ImageField(upload_to='course_picture')),
            ],
        ),
    ]
