from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('create/', views.restaurant_create, name='restaurant_create'),
    path('detail/<int:pk>/', views.restaurant_detail, name='restaurant_detail'), 

    # 댓글
    path('detail/<int:res_id>/comment/create/', views.create_comment, name='create_comment'), 
    path('detail/<int:restaurant_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='delete_comment'),
    path('detail/<int:restaurant_id>/comment/<int:comment_id>/update/', views.comment_update, name='update_comment'),

    #식당 
    path('detail/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
    path('update/<int:pk>/', views.restaurant_update, name='restaurant_update'),
]