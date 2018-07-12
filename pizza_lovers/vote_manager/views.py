from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import HttpResponse
from vote_manager.utils.db_helpers import get_voters_dict, save_vote
from vote_manager.utils.cache_mem_helpers import PizzaCacheMem
from vote_manager.utils.cache_file_helpers import PizzaCacheFile
import json


def get_voters_top_ten(request):
    """
    @summary: read json data from cache and returns top ten voters
    @rtype: HttpResponse object, content-type: application/json
    @return: dictionary containing two lists: names and votes
    """

    obj_cache = PizzaCacheMem()
    data_container = obj_cache.get_top_voters()

    # if cache is cold, get data from DB and warm cache
    if not data_container['ids']:
        data_container = get_voters_dict()
        json_to_save = json.dumps(data_container)
        obj_cache.update_top_voters(json_to_save)

    return JsonResponse(data_container)


def home_page(request):
    return render(request, 'home_page.html')


@login_required
def send_vote(request):
    """
    @precondition: user is_authenticated is true
    @summary: vote is saved and total votes counter is incremented. Cache is updated.
    @rtype: HttpResponse object, content-type: text/html
    @return: string
    """

    obj_user = request.user
    obj_voter, created = save_vote(obj_user)

    obj_cache = PizzaCacheMem()
    dict_top_voters = obj_cache.get_top_voters()

    # calling DB and warming cache only if user is in top X, or cache is cold
    if obj_user.id in dict_top_voters['ids'] or not dict_top_voters['ids']:
        data_container = get_voters_dict()
        json_to_save = json.dumps(data_container)
        obj_cache.update_top_voters(json_to_save)

    status = "Another vote, thanks again!" if not created else "Your first vote, thank you!"

    return HttpResponse(status)
