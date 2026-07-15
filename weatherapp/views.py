from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import WeatherReport
import requests
import os
def home(req):
    return render(req, "home.html")
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
def register_view(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        email = req.POST["email"]
        first_name = req.POST["first_name"]
        last_name = req.POST["last_name"]
        if User.objects.filter(username=username).exists():
            return render(
                req,
                "register.html",
                {
                    "error": "Username already exists"
                }
            )
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        return redirect("login")
    return render(req, "register.html")
def login_view(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(
            req,
            username=username,
            password=password
        )
        if user:
            login(req, user)
            req.session["username"] = user.username
            req.session["first_name"] = user.first_name
            req.session["last_name"]= user.last_name
            req.session["email"] = user.email
            return redirect("weather")
        return render(req, "login.html", {
            "error": "Invalid username or password"
        })
    return render(req, "login.html")
@login_required(login_url="login")
def weather_view(req):
    weather = None
    if req.method == "POST":
        city = req.POST.get("city")
        API_KEY = os.getenv("API_KEY")
        url = (
            f"http://api.weatherapi.com/v1/current.json?"
            f"key={API_KEY}&q={city}"
        )
        response = requests.get(url)
        weather = response.json()
        if "location" in weather:
            WeatherReport.objects.create(
                user=req.user,
                city=weather["location"]["name"],
                country=weather["location"]["country"],
                temperature=weather["current"]["temp_c"],
                humidity=weather["current"]["humidity"],
                wind_speed=weather["current"]["wind_kph"],
                condition=weather["current"]["condition"]["text"]
            )
    return render(
        req,
        "weather.html",
        {
            "weather": weather
        }
    )
@login_required(login_url="login")
def weather_history(req):
    reports = WeatherReport.objects.filter(
        user=req.user
    ).order_by("-id")
    return render(
        req,
        "history.html",
        {
            "reports": reports
        }
    )
@login_required(login_url="login")
def update_weather(req, id):
    report = get_object_or_404(
        WeatherReport,
        id=id,
        user=req.user
    )
    if req.method == "POST":
        report.city = req.POST.get("city")
        report.country = req.POST.get("country")
        report.temperature = req.POST.get("temperature")
        report.humidity = req.POST.get("humidity")
        report.wind_speed = req.POST.get("wind_speed")
        report.condition = req.POST.get("condition")
        report.save()
        return redirect("history")
    return render(
        req,
        "update_weather.html",
        {
            "report": report
        }
    )
@login_required(login_url="login")
def delete_weather(req, id):
    report = get_object_or_404(
        WeatherReport,
        id=id,
        user=req.user
    )
    report.delete()
    return redirect("history")
def logout_view(req):
    logout(req)
    req.session.flush()
    return redirect("home")