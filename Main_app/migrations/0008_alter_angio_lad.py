# Generated by Django 4.0.5 on 2022-07-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0007_alter_pci_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='angio',
            name='lad',
            field=models.TextField(default='Proximal: Normal /n Mid: Normal </br> Distal:Normal'),
        ),
    ]