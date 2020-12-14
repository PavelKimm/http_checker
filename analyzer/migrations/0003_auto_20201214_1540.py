# Generated by Django 3.1.4 on 2020-12-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0002_auto_20201214_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='websiteavailability',
            options={'ordering': ('website__url',), 'verbose_name_plural': 'Website availabilities'},
        ),
        migrations.AddField(
            model_name='websiteavailability',
            name='reason',
            field=models.TextField(default='OK'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='websiteavailability',
            name='server',
            field=models.CharField(default='nginx', max_length=200),
            preserve_default=False,
        ),
    ]