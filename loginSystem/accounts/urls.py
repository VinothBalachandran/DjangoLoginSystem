from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='loginpage'),
    path('logout/',views.logoutpage, name='logout'),
    path('home/',views.home,name='home'),
]
