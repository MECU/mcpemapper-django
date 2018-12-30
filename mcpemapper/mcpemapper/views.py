from django.http import HttpResponse
from .models import World
from django.contrib.auth.models import User


def detail(request, user_name, world_name):
    return HttpResponse(f"You're looking at world {world_name} owned by {user_name}")


def listUserWorlds(request, user_name):
    listingUser = User.objects.filter(username=user_name)
    return HttpResponse(listingUser)
    worlds = World.objects.filter(owner=listingUser, public=True)
    output = ', '.join([world.name for world in worlds])
    return HttpResponse(output)
