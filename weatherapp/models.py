from django.db import models
from django.contrib.auth.models import User
class WeatherReport(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    humidity = models.IntegerField()
    wind_speed = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    condition = models.CharField(max_length=100)
    searched_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.city