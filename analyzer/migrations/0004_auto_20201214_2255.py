# Generated by Django 3.1.4 on 2020-12-14 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0003_auto_20201214_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='websiteavailability',
            options={'ordering': ('website__url', '-id'), 'verbose_name_plural': 'Website availabilities'},
        ),
        migrations.RemoveField(
            model_name='websiteavailability',
            name='timeout',
        ),
    ]
