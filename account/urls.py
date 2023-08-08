from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/guest_login', views.guest_login, name='guest_login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

]
