from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('createvideocall/', views.create_video, name='createvideocall'),
    path('joinvideocall/', views.join_video, name='joinvideocall'),
    path('logout', views.logout_view, name='logout')
]