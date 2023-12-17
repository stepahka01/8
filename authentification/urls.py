from django.urls import path
from . import views


urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
    path('update-profile', views.update_profile, name='update-profile'),
]
