# Generated by Django 2.0 on 2018-04-21 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node',
            options={'ordering': ['-show', 'order'], 'verbose_name_plural': '节点'},
        ),
        migrations.AddField(
            model_name='node',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='排序'),
        ),
    ]