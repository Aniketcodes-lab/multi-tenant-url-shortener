from django.db import models
from tenants.models import Tenant

class ShortURL(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="short_urls")
    original_url = models.URLField()
    short_code = models.CharField(max_length=10)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("tenant", "short_code")

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
