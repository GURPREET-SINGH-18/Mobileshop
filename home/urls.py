from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('login/login',views.login,name='login'),
    path('login/signup/',views.signup,name='signup'),
    path('learnmore/',views.learnmore,name='learnmore'),
    path('learnmore/login',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path("learnmore/products/<int:myid>", views.learnmore,name='learnmore'),
    path("learnmore/products/login", views.login,name='login'),
]
