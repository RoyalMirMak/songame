import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "songame.settings")
django.setup()

from quiz.models import Song


def fill_song():
    Song.objects.all().delete()
    songfile = open("song_list/song_list.txt", "r", encoding="utf8")
    lines = songfile.readlines()
    id = 1
    was = set()
    for i in range(0, len(lines), 4):
        name = lines[i + 2].strip()
        authors = lines[i + 1].strip()
        comb = (name, authors)
        if comb in was:
            continue
        Song.objects.create(song_id=id, name=name, authors=authors)
        was.add(comb)
        id += 1


fill_song()