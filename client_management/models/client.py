from django.db import models

from client_management.enums import Gender


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    bank_account_number = models.CharField(max_length=50, blank=True, null=True)
    title = models.ForeignKey("ClientTitle", on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    first_name_ar = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    family_name_ar = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    address_ar = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=Gender.get_choices())
    birth_date = models.DateField(blank=True, null=True)
    unique_code = models.CharField(max_length=50, unique=True)
    client_type = models.ForeignKey("ClientType", on_delete=models.PROTECT)
    client_nature = models.ForeignKey("ClientNature", on_delete=models.SET_NULL, null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    marketing_referral = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.family_name}"
