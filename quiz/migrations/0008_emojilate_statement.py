# Generated by Django 3.2.18 on 2023-07-23 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_emojilate'),
    ]

    operations = [
        migrations.AddField(
            model_name='emojilate',
            name='statement',
            field=models.TextField(default='Ниже приведён отрывок из какого-то трека, переведённый на язык эмоджи. Угадайте этот трек!', editable=False),
        ),
    ]
