# Generated by Django 3.2.9 on 2021-12-12 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricetable',
            old_name='pc_new_price',
            new_name='pt_new_price',
        ),
        migrations.RenameField(
            model_name='pricetable',
            old_name='pc_old_price',
            new_name='pt_old_price',
        ),
        migrations.RenameField(
            model_name='pricetable',
            old_name='pc_title',
            new_name='pt_title',
        ),
    ]