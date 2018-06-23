from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Voter(models.Model):
    id_voter = models.AutoField(primary_key=True)
    fko_user = models.ForeignKey(User,
                                db_column="fk_user",
                                 on_delete=models.CASCADE)
    vote_counter = models.IntegerField()

    class Meta:
        db_table = 'pizza_voter'