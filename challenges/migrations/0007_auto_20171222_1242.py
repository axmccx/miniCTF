# Generated by Django 2.0 on 2017-12-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0006_auto_20171222_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
