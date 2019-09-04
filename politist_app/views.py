from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from . import forms
from politist_app.models import Search
from politist_app.forms import SearchForm
from django.views.generic import (View, TemplateView, DetailView, CreateView)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from politist_app.utils import get_tweets, sentiment_analyser, toi, get_related_tweets
import requests
import json


tweet_list = []
tweet_data = []
s = ''

class LogoutSuccessView(TemplateView):
    template_name = 'politist_app/app_templates/logout_success.html'

class IndexView(TemplateView):
    template_name = 'politist_app/app_templates/index.html'

class SignupView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'politist_app/registration/signup.html'


@login_required
def DashboardView(request):
    global tweet_list
    global tweet_data
    toi_list = toi()
    form = SearchForm()
    toi_list = toi()
    if request.method == "POST":
        form = SearchForm(request.POST)
        
        if form.is_valid():
            global s
            s = form.save(commit=True)
            
            tweet_list = get_tweets(str(s))
            tweet_data = get_related_tweets(str(s))
            return render(request, 'politist_app/app_templates/tweet_list.html', {'tweet_list': tweet_list, 's': s, 'tweet_data': tweet_data})
        else:
            print("Invalid Form!")

    return render(request, 'politist_app/app_templates/dashboard.html', {'form': form, 'toi_list': toi_list})
    
@login_required
def AnalyticsView(request):
    global tweet_list
    global tweet_data
    global s
    emotion, score, emotion_dict, reaction = sentiment_analyser(tweet_list)
    return render(request, 'politist_app/app_templates/analytics.html', {'score': score, 'emotion': emotion,"emotion_dict": emotion_dict, 'reaction': reaction, 's': s})