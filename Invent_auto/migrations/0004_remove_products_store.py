# Generated by Django 3.2.6 on 2021-08-20 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invent_auto', '0003_alter_products_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Store',
        ),
    ]