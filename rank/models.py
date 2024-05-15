from django.db import models
from django.contrib.auth.models import User

class Rank(models.Model):
    usuario = models.CharField(max_length=100, default=None)
    tag = models.CharField(max_length=100, default='BR1')
    tier = models.CharField(max_length=30, default='Unranked')
    rank = models.CharField(max_length=10, default='Unranked')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    league_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.usuario} ({self.tag}) - {self.tier} {self.rank} {self.user}"
    
