# Generated by Django 4.0.5 on 2022-07-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0005_alter_angio_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pci',
            name='result_pci',
            field=models.CharField(default=' Successful PCI done to', max_length=100),
        ),
    ]