# Generated by Django 5.0.6 on 2024-06-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_alter_stafnotificatuion_crated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='stafnotificatuion',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
