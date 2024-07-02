from django.db import models


class ToDo(models.Model):
    activity = models.CharField(max_length=200)

    def __str__(self):
        return self.activity