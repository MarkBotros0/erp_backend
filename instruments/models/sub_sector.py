from django.db import models


class SubSector(models.Model):
    sector = models.ForeignKey("Sector", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.sector.name} - {self.name}"
