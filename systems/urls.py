from os import name
from django.urls import path
from users.views import *

app_name = 'profiles'

urlpatterns = [
    path('', p_profile, name="profile_def"),
    path('<int:pk>', ProfileUpdateView.as_view() ,name="profile_default"),
    path('settings/<int:pk>', settingUpdateView.as_view(),name="settings")
]
