from django.db import models


class ClientTitle(models.Model):
    title = models.CharField(max_length=20)
    title_ar = models.CharField(max_length=20)

    def __str__(self):
        return self.title
