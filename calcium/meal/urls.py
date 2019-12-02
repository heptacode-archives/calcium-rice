from django.urls import path
from meal import views

app_name = 'meal'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    # path('/', views.meal, name='meal'),
    # path('<int:question_id>/results', views.results, name='results'),
    # path('<int:question_id>/vote', views.vote, name='vote')
]