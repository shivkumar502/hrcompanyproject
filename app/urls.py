from django.urls import path
from .views import *
urlpatterns = [
    path("register/",register_user,name="register-user"),
    path('login/',login_user,name='login-user'),
    path('event/',create_event,name="create-events")
]
