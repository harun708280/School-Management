# Generated by Django 5.0.6 on 2024-06-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_customuser_user_type_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile pic'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'STAFF'), (3, 'STUDENT')], default=1, max_length=50, null=True),
        ),
    ]
