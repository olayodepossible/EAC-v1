from django.shortcuts import render


# Create your views here.

rooms = [
    {'id': 1, 'name': "check1"},
    {'id': 2, 'name': "check2"},
    {'id': 3, 'name': "check3"},
]


def home(req):
    context = {'rooms': rooms}
    return render(req, 'base/home.html', context)


def room(req, key):
    class_room = None
    for i in rooms:
        if i['id'] == int(key):
            class_room = i
    context = {'room': class_room}
    return render(req, 'base/room.html', context)

def createRoom(req):
    context = {}
    return render(req, 'base/room_form.html', context)