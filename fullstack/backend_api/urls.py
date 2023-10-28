from django.urls import path
from . import views

urlpatterns = [
    path('bots/<str:username>/', views.BotsView.as_view(), name='bots'),
    path('users/', views.UsersView.as_view(), name='users')
    
]
