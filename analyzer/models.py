from django.db import models


class Website(models.Model):
    url = models.CharField(max_length=2048, unique=True)
