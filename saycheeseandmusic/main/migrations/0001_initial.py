# Generated by Django 4.0.3 on 2022-04-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='suicideBoys',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('singer', models.CharField(max_length=2000)),
                ('album', models.CharField(max_length=2000)),
                ('song_img', models.ImageField(upload_to='images')),
                ('song_file', models.FileField(upload_to='images')),
            ],
        ),
    ]