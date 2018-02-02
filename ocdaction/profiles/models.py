from __future__ import unicode_literals
from django.db import models
from custom_user.models import AbstractEmailUser


class OCDActionUser(AbstractEmailUser):
    """ User is authenticated with their email
    but for app purposes users also have usernames.
    """
    nickname = models.CharField(max_length=24, null=True)
    date_birth = models.DateField('date of birth', null=True)
    have_ocd = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
