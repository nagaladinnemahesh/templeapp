# In pilgrimage/urls.py
from django.urls import path
from . import views
from .views import logout_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .views import CustomLoginView

app_name = 'pilgrimage'

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage is the default view
    path('logout/', logout_view, name='logout'),
    path('login/', CustomLoginView.as_view(), name='user_login'),
    path('book/', views.book_ticket, name='book_ticket'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('booking_history/', views.booking_history, name='booking_history'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', logout_view, name='logout'),
]
