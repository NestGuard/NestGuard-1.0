# Generated by Django 5.1.4 on 2024-12-22 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppNestGuard', '0006_nestguardcontatopage_descricao10_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NestGuardContatoPage',
        ),
        migrations.DeleteModel(
            name='NestGuardDashboradPage',
        ),
        migrations.DeleteModel(
            name='NestGuardSegurançaPage',
        ),
        migrations.DeleteModel(
            name='NestGuardSitesPage',
        ),
        migrations.DeleteModel(
            name='NestGuardSobrePage',
        ),
    ]
