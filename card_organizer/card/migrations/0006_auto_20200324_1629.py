# Generated by Django 3.0.4 on 2020-03-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_pokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]
