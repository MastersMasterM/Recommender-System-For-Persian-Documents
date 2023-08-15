"""
Defining Database Schema
"""
from django.db import models


class Paper(models.Model):
    uid = models.CharField(max_length=12)
    title = models.TextField()
    abstract = models.TextField()
    fl_subject = models.TextField()
    sl_subject = models.TextField()

    def __str__(self) -> str:
        return self.title
