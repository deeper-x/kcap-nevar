from django.db import models
from django.contrib.auth.models import User


class Voter(models.Model):
    id_voter = models.AutoField(primary_key=True)
    fko_user = models.OneToOneField(User,
                                    db_column="fk_user",
                                    unique=True,
                                    on_delete=models.CASCADE)
    vote_counter = models.IntegerField()

    class Meta:
        db_table = 'pizza_voter'
