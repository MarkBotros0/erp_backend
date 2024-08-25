from django.db import models


class TimestampsAbstractModel(models.Model):
    """
    An abstract model for created at and updated at timestamps
    """

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True
