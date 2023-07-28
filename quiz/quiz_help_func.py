from .models import Zapunch, Song, Emojilate
from .views import tasks_num, puzzle_data, tasklist, right_answers_num, task_id, tasks_left, user_tasks_num, user_quiz_type
import random

def get_action(tasks_left):
    if tasks_left == 1:
        return "result"
    else:
        return "puzzle"


def setup(request):
    global tasks_num, puzzle_data, tasklist, right_answers_num, task_id, tasks_left, user_tasks_num, user_quiz_type
    user_tasks_num = int(request.POST.get("task_num"))
    user_quiz_type = request.POST.get("quiz_type", "mix")
    tasks_num = user_tasks_num
    tasks_left = tasks_num
    right_answers_num = 0
    task_id = 0
    songlist = list(Song.objects.in_bulk().values())
    songlist.sort(key=lambda x: (x.name, x.authors))
    if user_quiz_type == "zapunch":
        tasklist = list(Zapunch.objects.in_bulk().values())
    else:
        tasklist = list(Emojilate.objects.in_bulk().values())
    random.shuffle(tasklist)
    puzzle_data = {"task": tasklist[0], "action": get_action(tasks_left), "type": user_quiz_type, "songs": songlist}


def is_answer_right(request, task):
    if task.type == "zapunch":
        return request.POST.get("user_answer") == puzzle_data["task"].answer
    elif task.type == "emojilate":
        return request.POST.get("user_answer") == str(puzzle_data["task"].answer_id)


def handle(request):
    global puzzle_data, task_id, right_answers_num, tasks_left
    if request.POST.get("start", "undefined") == "true":
        setup(request)
    else:
        if is_answer_right(request, puzzle_data["task"]):
            right_answers_num += 1
        tasks_left -= 1
        puzzle_data["action"] = get_action(tasks_left)
        task_id += 1
    if task_id < tasks_num:
        puzzle_data["task"] = tasklist[task_id]