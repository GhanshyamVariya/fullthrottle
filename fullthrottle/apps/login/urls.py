from django.conf.urls import url

from fullthrottle.apps.login import views

urlpatterns = [
    url('users/register/', views.register, name='register'),
    url('users/login/', views.login, name='login'),
    url('users/logout/', views.logout, name='logout')
]
