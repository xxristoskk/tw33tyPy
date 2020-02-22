from django.db import models
from django.utils import timezone
from django_plotly_dash import DjangoDash
import datetime

class StatelessApp(models.Model):
    app_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    def as_dash_app(self):
        return app_name
