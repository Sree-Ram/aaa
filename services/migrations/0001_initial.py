# Generated by Django 3.2.2 on 2021-05-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=1000)),
                ('img', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
