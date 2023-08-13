from django.db import models


class RandomNumber(models.Model):
    number = models.IntegerField(null=True)