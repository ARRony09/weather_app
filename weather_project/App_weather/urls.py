from . import views
from django.urls import path


app_name='App_weather'
urlpatterns = [
    path('',views.index,name='index')
]