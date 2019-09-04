from django.contrib import admin
from django.urls import path, include
from politist_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('politist/', include('politist_app.urls')),
    path('politist/', include('django.contrib.auth.urls')),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('logout_success/', views.LogoutSuccessView.as_view(), name='logout_success'),
    path('login_success/', views.LoginSuccessView.as_view(), name='login_success'),
]