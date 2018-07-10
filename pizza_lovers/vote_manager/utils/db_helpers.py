from ..models import Voter
from django.db.models import F


def get_voters_dict(tot=10):
    """
    @summary: fetch top ten voters from DB, creating two list (votes and labels)
    @param tot: number of entries to be read
    @rtype: dict
    @return: dictionary containing two lists: names and votes
    """
    list_votes, list_names = [], []
    qs_votes = Voter.objects.all().order_by('-vote_counter')[:tot]

    for i in qs_votes:
        list_votes.append(i.vote_counter)
        list_names.append(i.fko_user.username)

    dict_container = {'names': list_names,
                      'votes': list_votes}

    return dict_container


def save_vote(obj_user):
    """
    @summary: given an user, save his vote incrementing counter
    @param obj_user: session user in request
    @return: tuple with "voter object" and "has been created" bool flag
    """
    obj_voter, created = Voter.objects.get_or_create(
                                    fko_user=obj_user,
                                    defaults={'vote_counter': 0}
                                    )

    obj_voter.vote_counter = F('vote_counter') + 1
    obj_voter.save()

    return obj_voter, created
