from django.urls import path
from . import views
from . import views
urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name="register"),

    path('home/<str:username>',views.home, name='home'),
]
