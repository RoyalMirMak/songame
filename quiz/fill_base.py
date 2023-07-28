import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "songame.settings")
django.setup()

from quiz.models import Zapunch, Emojilate, Neurocover


def fill_zapunch():
    Zapunch.objects.all().delete()
    punchfile = open("task_stubs/zapunch_stubs.txt", "r", encoding="utf8")
    lines = punchfile.readlines()
    str_now = ""
    for line in lines:
        if line.strip() == "":
            if str_now != "":
                str_now = str_now.strip()
                parts = str_now.split("#")
                given = []
                missed = []
                for i in range(len(parts)):
                    if i % 2 == 0 and str_now[0] != "#" or i % 2 == 1 and str_now[0] == "#":
                        given.append(parts[i])
                    else:
                        missed.append(parts[i])
                #punch_tasks.append(task_fill_in(given, missed))
                Zapunch.objects.create(part1=given[0], answer=missed[0], part2=given[1])
            str_now = ""
        else:
            str_now += line
            str_now += "<br>"
    punchfile.close()


def fill_emojilate():
    Emojilate.objects.all().delete()
    emojifile = open("task_stubs/emojilate_stubs.txt", "r", encoding="utf8")
    lines = emojifile.readlines()
    str_now = ""
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line[0:2] == "##":
            id_now = int(line[2:-2])
            str_now = str_now.strip()
            if str_now != "":
                Emojilate.objects.create(text=str_now, answer_id=id_now)
            str_now = ""
        else:
            str_now += line
            str_now += "<br>"
    emojifile.close()


def fill_neurocover():
    Neurocover.objects.all().delete()
    coverfile = open("task_stubs/neurocover_stubs.txt", "r", encoding="utf8")
    lines = coverfile.readlines()
    str_now = ""
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line[0:2] == "##":
            id_now = int(line[2:-2])
            str_now = str_now.strip()
            if str_now != "":
                str_now = "/static/images/neurocover/" + str_now
                Neurocover.objects.create(image_path=str_now, answer_id=id_now)
            str_now = ""
        else:
            str_now += line
    coverfile.close()


fill_zapunch()
fill_emojilate()
fill_neurocover()