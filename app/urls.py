from django.urls import path
from app.views.views import *
from app.views.custom_exceptions import *

app_name = "main_app"


urlpatterns = [
    path('', index, name='index'),
    path('playstation5/', playstation5, name='playstation5'),
    path('switch/', switch, name='switch'),
    path('xbox/', xbox, name='xbox'),
    path('donate/', donate, name='donate'),
    path('about/', about, name='about'),
    path('delete_product/<int:id>', delete_product, name='delete_product'),
]
