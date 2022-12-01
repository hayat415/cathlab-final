# Generated by Django 4.0.5 on 2022-11-28 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='procedure',
        ),
        migrations.AddField(
            model_name='pci',
            name='pci',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Main_app.procedure'),
        ),
    ]
