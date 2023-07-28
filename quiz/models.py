from django.db import models


class Zapunch(models.Model):
    statement = models.TextField(default="Ниже приведён отрывок из какого-то трека. Подумайте как автор и дополните панч!", editable=False)
    part1 = models.TextField()
    answer = models.TextField()
    part2 = models.TextField()
    type = models.TextField(default="zapunch", editable=False)


class Song(models.Model):
    song_id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    authors = models.TextField()
    #album = models.TextField()
    #duration = models.DurationField()


class Emojilate(models.Model):
    statement = models.TextField(default="Ниже приведён отрывок из какого-то трека, переведённый на язык эмоджи. Угадайте этот трек!", editable=False)
    text = models.TextField()
    answer_id = models.IntegerField()
    type = models.TextField(default="emojilate", editable=False)


class Neurocover(models.Model):
    statement = models.TextField(default="Вы видите обложку некоторого трека, которая была сгенерирована при помощи нейросетей. Угадайте, что это за трек!", editable=False)
    image_path = models.TextField()
    answer_id = models.IntegerField()
    type = models.TextField(default="neurocover", editable=False)