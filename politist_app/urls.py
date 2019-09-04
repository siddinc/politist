from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'politist_app'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='politist_app/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('analytics/', views.AnalyticsView, name='analytics'),
    path('tweetlist/', views.TweetListView, name='tweet_list'),
    path('tweetlist/', views.TweetListView, name='tweet_list')
]