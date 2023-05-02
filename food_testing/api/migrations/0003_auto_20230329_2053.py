# Generated by Django 3.2.8 on 2023-03-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_fooditem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fooditem',
            options={'verbose_name': 'Food', 'verbose_name_plural': 'Foods'},
        ),
        migrations.AlterField(
            model_name='fooddata',
            name='humidity',
            field=models.DecimalField(db_column='humidity', decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='fooddata',
            name='methane',
            field=models.DecimalField(db_column='methane', decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='fooddata',
            name='temperature',
            field=models.DecimalField(db_column='temperature', decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterModelTable(
            name='fooditem',
            table='Food',
        ),
    ]
