from . import views
from django.urls import path


app_name='App_login'
urlpatterns = [
    path('',views.sign_up,name='sign_up'),
    path('login/',views.login_form,name='login'),
    path('logout/',views.logout_user,name='logout'),
]
