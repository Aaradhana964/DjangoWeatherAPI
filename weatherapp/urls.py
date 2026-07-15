from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path( "register/",views.register_view,name="register"),
    path( "login/",views.login_view,name="login"),
    path( "weather/", views.weather_view,name="weather"),
    path( "history/", views.weather_history,name="history"),
    path("update/<int:id>/",views.update_weather,name="update_weather"),
    path("delete/<int:id>/",views.delete_weather,name="delete_weather"),
    path("logout/",views.logout_view,name="logout"),]