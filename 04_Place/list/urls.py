from django.urls import path
from . import views

urlpatterns = [
    path('', views.f_list, name='f_list'),
    path('<int:pk>/', views.f_detail, name='f_detail'),
    path('post/', views.f_post, name='f_post'),
    path('<int:pk>/edit/', views.f_edit, name='f_edit'),
    path('<int:pk>/delete/', views.f_delete, name='f_delete')
]