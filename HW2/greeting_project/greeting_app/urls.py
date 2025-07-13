from django.urls import path
from .views import home,greet
app_name = "greeting_app"
urlpatterns = [
    path('', home, name="home"),
    path('greet/<str:name>/', greet, name="greet_with_name"),
    path('greet/', greet, name='greet'),
]