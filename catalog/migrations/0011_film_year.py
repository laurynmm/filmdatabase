# Generated by Django 3.2.6 on 2021-08-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20210806_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.IntegerField(default=1900),
            preserve_default=False,
        ),
    ]