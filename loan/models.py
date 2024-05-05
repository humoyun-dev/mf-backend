from django.db import models
from users.models import CustomUser
import datetime
# Create your models here.

class Loan(models.Model):
    loan_name = models.CharField(max_length=255)
    loan_value = models.BigIntegerField()
    get_loan_date = models.DateField(default=datetime.datetime.now())
    give_loan_date = models.DateField()
    owner = models.ForeignKey(CustomUser, related_name="owner", on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.loan_name} by {self.owner}"
