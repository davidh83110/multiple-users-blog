# Generated by Django 2.1 on 2019-12-13 08:22

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20191213_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
