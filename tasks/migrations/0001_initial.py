# Generated by Django 3.1.1 on 2020-09-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('pub_date', models.DateTimeField(verbose_name='Publication Date')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
            ],
        ),
    ]
