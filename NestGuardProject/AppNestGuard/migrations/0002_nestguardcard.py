# Generated by Django 5.1.1 on 2024-10-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNestGuard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NestGuardCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('descricao', models.TextField()),
                ('link_img', models.URLField()),
            ],
        ),
    ]
