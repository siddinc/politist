from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib import auth


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username

class Search(models.Model):
    topic_search = models.CharField(max_length = 100, verbose_name='Topic Search')

    def __str__(self):
        return self.topic_search

        #model