from django.shortcuts import render


# Create your views here.

rooms = [
    {'id': 1, 'name': "check1"},
    {'id': 2, 'name': "check2"},
    {'id': 3, 'name': "check3"},
]


def home(req):
    return render(req, 'base/home.html', {'rooms': rooms})


def room(req):
    return render(req, 'base/room.html', {'rooms': rooms})
