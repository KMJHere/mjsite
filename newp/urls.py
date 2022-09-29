from django.urls import path

from . import views

app_name = 'newp'

urlpatterns = [
    # url: /newp/
    path('', views.index, name='index'),
    # url: /newp/1/
    path('<int:member_id>/', views.detail, name='detail'),
    # url: /newp/1/modify/
    path('<int:member_id>/modify/', views.modify, name='modify'),
    # url: /newp/1/like/
    path('<int:board_id>/like/', views.like, name='like'), 
     # url: /newp/1/like/
    path('<int:board_id>/result/', views.result, name='result') 

]