from django.shortcuts import render, redirect
from .forms import RoomForm
from .models import Room, Topic

# Create your views here.

rooms = [
    {'id': 1, 'name': "check1"},
    {'id': 2, 'name': "check2"},
    {'id': 3, 'name': "check3"},
]


def home(req):
    req_param = req.GET.get('q') if req.GET.get('q') != None else ''
    class_rooms = Room.objects.filter(topic__name__icontains=req_param)  # icontains = search with ignoreCase
    class_topics = Topic.objects.all()
    context = {'rooms': class_rooms, 'topics': class_topics}
    return render(req, 'base/home.html', context)


def room(req, key):
    class_room = Room.objects.get(id=key)

    context = {'room': class_room}
    return render(req, 'base/room.html', context)


def create_room(req):
    form = RoomForm()
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'topics': form['topic']}
    return render(req, 'base/room_form.html', context)


def update_room(req, key):
    class_room = Room.objects.get(id=key)
    form = RoomForm(instance=class_room)
    if req.method == 'POST':
        form = RoomForm(req.POST, instance=class_room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(req, 'base/room_form.html', context)


def delete_room(req, key):
    class_room = Room.objects.get(id=key)
    if req.method == 'POST':
        class_room.delete()
        return redirect('home')
    return render(req, 'base/delete.html', {'obj': class_room})
