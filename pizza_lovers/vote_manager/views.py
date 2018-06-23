from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from vote_manager.models import Voter
from json import dumps


@login_required
def get_voters_top_ten(request):
    qs_votes = Voter.objects.values_list('vote_counter', flat=True)

    # in order queryset to be serializable, convert it to list
    ret_votes = list(qs_votes)

    return JsonResponse(ret_votes,safe=False)


@login_required
def home_page(request):
    return render(request, 'home_page.html')