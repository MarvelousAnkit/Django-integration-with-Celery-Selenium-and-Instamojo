# Generated by Django 4.1.7 on 2023-03-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Phone', models.CharField(max_length=50)),
                ('Copies', models.CharField(max_length=50)),
                ('Page_Limit', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=100)),
                ('delivery', models.CharField(max_length=100)),
                ('Files1', models.FileField(default=None, max_length=2000, null=True, upload_to='')),
                ('Payment_id', models.CharField(max_length=200)),
                ('Paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
