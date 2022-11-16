from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete'),
    path('update_post/<int:post_id>/', views.update_post, name='update'),
]
