from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import F

from vote_manager.models import Voter
from django.http.response import HttpResponse


def get_voters_top_ten(request):
    """
    @summary: fetch top ten voters from DB, creating two list (votes and labels)
    @rtype: applcation/json
    @return: dictionary containing two lists: names and votes
    """
    list_votes, list_names = [], []
    qs_votes = Voter.objects.all().order_by('-vote_counter')[:10]

    for i in qs_votes:
        list_votes.append(i.vote_counter)
        list_names.append(i.fko_user.username)

    data_container = {'names': list_names,
                      'votes': list_votes}

    return JsonResponse(data_container)


def home_page(request):
    return render(request, 'home_page.html')


@login_required
def send_vote(request):
    """
    @precondition: user is_authenticated is true
    @summary: vote is saved and total votes counter is incremented
    @rtype: HttpResponse object
    @return: string
    """
    obj_user = request.user

    obj_voter, created = Voter.objects.get_or_create(
                                    fko_user=obj_user,
                                    defaults={'vote_counter': 0}
                                    )

    obj_voter.vote_counter = F('vote_counter') + 1
    obj_voter.save()

    status = "Vote sent. Thank you!"

    return HttpResponse(status)
