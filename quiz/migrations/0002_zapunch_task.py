# Generated by Django 3.2.18 on 2023-07-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapunch',
            name='task',
            field=models.TextField(default='Ниже приведён отрывок из какого-то трека. Подумайте как автор и дополните панч!', editable=False),
        ),
    ]
