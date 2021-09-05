from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view),
    path('register', views.register_view),
    path('login', views.login_view),
    path('user_center', views.user_center_view),
    path('quit', views.quit_view),
]