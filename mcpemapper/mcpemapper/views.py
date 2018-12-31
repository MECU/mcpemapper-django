from django.http import HttpResponse, Http404
from .models import World
from django.contrib.auth.models import User
from django.template import loader
import subprocess


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mcpemapper/index.html')
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, user_name, world_name):
    return HttpResponse(f"You're looking at world {world_name} owned by {user_name}")


def listUserWorlds(request, user_name):
    listingUser = User.objects.filter(username=user_name)
    if not listingUser:
        raise Http404

    worlds = World.objects.filter(owner=listingUser[0], public=True)
    template = loader.get_template('mcpemapper/user.html')
    context = {
        'user': listingUser[0],
        'worlds': worlds,
    }

    return HttpResponse(template.render(context, request))


def processWorld(request):
    user = request.User
    world = request.World
    # ./ mcpe_viz - -db / home / rpn / ownclouddata / mecu / files / minecraft / QmQCAFBwFAA\= / --out / home / rpn / www / minecraft / mecu / stronghold - -html - all - -quiet - -all - image
    subprocess.call("./mcpe_viz --db /home/MECU/mcpemapper/mcpemapper/worlds/{{user.username}}/{{world.name}} --out /home/MECU/mcpemapper/mcpemapper/worlds/{{user.username}}/{{world.name}}/{{world.name}} --html-all --quiet --all-image 1>$HOME/out 2>$HOME/error", shell=True)
    return True
