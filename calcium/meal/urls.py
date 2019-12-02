from django.urls import path
from meal import views

app_name = 'meal'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail', views.DetailView.as_view(), name='detail'),
]