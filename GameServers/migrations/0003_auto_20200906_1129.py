# Generated by Django 2.2.15 on 2020-09-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameServers', '0002_auto_20200906_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minecraft',
            name='server_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='minecraft',
            name='server_version',
            field=models.TextField(blank=True, null=True),
        ),
    ]