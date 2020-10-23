from django.contrib.auth.models import AbstractUser, Group
from rest_framework import serializers
from .models import *


class UserDetailsSerializers(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'


class ExpensesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Expenses
		fields = '__all__'


class ReminderSerializers(serializers.ModelSerializer):
	class Meta:
		model = Reminder
		fields = '__all__'


class BillMonitorSerializers(serializers.ModelSerializer):
	class Meta:
		model = BillMonitor
		fields = '__all__'


class PayCheckSerializers(serializers.ModelSerializer):
	class Meta:
		model = PayCheck
		fields = '__all__'


class CashFlowSerializers(serializers.ModelSerializer):
	class Meta:
		model = CashFlow
		fields = '__all__'
