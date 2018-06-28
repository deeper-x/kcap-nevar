from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import F

from vote_manager.models import Voter
from django.http.response import HttpResponse


def get_voters_top_ten(request):
    qs_votes = Voter.objects.all().order_by('-vote_counter')[:10]

    list_votes = [i.vote_counter for i in qs_votes]
    list_names = [y.fko_user.username for y in qs_votes]

    data_container = [list_names, list_votes]

    return JsonResponse(data_container, safe=False)


def home_page(request):
    return render(request, 'home_page.html')


def send_vote(request):
    if request.user.is_authenticated:
        obj_user = request.user

        obj_voter, created = Voter.objects.get_or_create(
                                    fko_user=obj_user,
                                    defaults={'vote_counter': 0}
                                    )

        obj_voter.vote_counter = F('vote_counter') + 1
        obj_voter.save()

    return HttpResponse("vote request sent")
