# Generated by Django 3.2.18 on 2023-07-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_neurocover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neurocover',
            name='type',
            field=models.TextField(default='neurocover', editable=False),
        ),
    ]