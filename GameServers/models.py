from django.db import models


# Create your models here.

class Minecraft(models.Model):
    server_name = models.CharField(max_length=120)
    server_version = models.TextField(blank=True, null=True)
    server_ip = models.TextField()
    server_png = models.TextField()
    server_time = models.DurationField()
