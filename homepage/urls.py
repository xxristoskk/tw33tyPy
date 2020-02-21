from django.urls import path
from . import views
from homepage.dash_apps.finished_apps import bar, sentiment


app_name = 'homepage'
urlpatterns = [
    path('',views.home, name='home'),

]
