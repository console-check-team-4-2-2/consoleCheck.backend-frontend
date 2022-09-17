from django.urls import path
from .views import *

app_name = "auth"

urlpatterns = [
    path('login/', login_user, name='login'),
    # path('registration/', registration_user, name='registration'),
    path('logout/', logout_user, name='logout'),
]
