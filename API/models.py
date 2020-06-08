from django.db import models
from django.core.validators import MinLengthValidator,MinValueValidator


# Create your models here.
class UserATM(models.Model):
    user_card = models.CharField(max_length=8,unique=True,validators=[MinLengthValidator(
        limit_value=8,
        message = "Input 8 digit card number",
        )])
    pin = models.CharField(max_length=4,validators=[MinLengthValidator(
        limit_value=4,
        message = "Input 4 digit pin",
        )])
    balance = models.DecimalField(default=float(0),max_digits=50,decimal_places=2,validators=[MinValueValidator(float(0))])



