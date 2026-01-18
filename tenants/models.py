from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=255, unique=True)
    app_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)
    primary_color = models.CharField(max_length=20, default="#000000")

    def __str__(self):
        return self.name
