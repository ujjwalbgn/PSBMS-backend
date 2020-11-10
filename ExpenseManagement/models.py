from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):

    phone = models.CharField(max_length=13, blank=True)
    address = models.CharField(max_length=200, blank=True)
    date_created = models.DateField(auto_now_add=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.firstname and self.lastname:
            display = (self.firstname + " " + self.lastname)
        else:
            display = str(self.date_created)
        return display


class Expenses(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(blank=True, null=True,  max_digits=19, decimal_places=2)
    dateTime = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.title


class Reminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    reminderDateTime = models.DateTimeField(blank=True, default=datetime.now)
    createDateTime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


class BillMonitor(models.Model):
    BOOL_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    FREQUENCY_CHOICES = [('Weekly', 'Weekly'), ('BiWeekly', 'BiWeekly'), ('Monthly', 'Monthly'),
                         ('Quarterly','Quarterly'),('Semiannually','Semiannually'),('Annually','Annually')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    dueDateTime = models.DateTimeField(blank=True, default=datetime.now)
    amount = models.DecimalField(blank=True, null=True,  max_digits=19, decimal_places=2)
    recursive = models.CharField(max_length=5, choices=BOOL_CHOICES,null=True)
    recursiveFrequency = models.CharField(max_length=15, choices=FREQUENCY_CHOICES,null=True)

    def __str__(self):
        return self.title


class PayCheck(models.Model):
    BOOL_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    FREQUENCY_CHOICES = [('Weekly', 'Weekly'), ('BiWeekly', 'BiWeekly'), ('Monthly', 'Monthly'),
                         ('Quarterly','Quarterly'),('Semiannually','Semiannually'),('Annually','Annually')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    payDateTime = models.DateTimeField(blank=True, default=datetime.now)
    recursive = models.CharField(max_length=5, choices=BOOL_CHOICES,null=True)
    amount = models.DecimalField(blank=True, null=True,  max_digits=19, decimal_places=2)
    recursiveFrequency = models.CharField(max_length=15, choices=FREQUENCY_CHOICES,null=True)

    def __str__(self):
        return self.title


class CashFlow(models.Model):
    BOOL_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    FREQUENCY_CHOICES = [('Weekly', 'Weekly'), ('BiWeekly', 'BiWeekly'), ('Monthly', 'Monthly'),
                         ('Quarterly','Quarterly'),('Semiannually','Semiannually'),('Annually','Annually')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    payDateTime = models.DateTimeField(blank=True, default=datetime.now)
    recursive = models.CharField(max_length=5, choices=BOOL_CHOICES,null=True)
    amount = models.DecimalField(blank=True, null=True,  max_digits=19, decimal_places=2)
    recursiveFrequency = models.CharField(max_length=15, choices=FREQUENCY_CHOICES,null=True)

    def __str__(self):
        return self.title


class Inventory(models.Model):
    BOOL_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    name = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    cost_price = models.DecimalField(blank=True, null=True,  max_digits=19, decimal_places=2)
    last_modified = models.DateField(auto_now_add=True)
    barcode = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    restock = models.CharField(max_length=5, choices=BOOL_CHOICES,null=True)
    restock_quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
