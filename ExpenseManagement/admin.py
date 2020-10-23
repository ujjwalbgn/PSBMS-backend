from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CustomUser)
admin.site.register(Expenses)
admin.site.register(Reminder)
admin.site.register(BillMonitor)
