from django.urls import path
from meal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/today', views.today, name='today'),
    path('/yesterday', views.yesterday, name='yesterday'),
]