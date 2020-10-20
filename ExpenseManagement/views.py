from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import *
from .models import *


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'paycheck': reverse('paycheck-list', request=request, format=format),
        # 'reminder': reverse('reminder-list', request=request, format=format)
    })

# Class based views
class PayCheckViewSet(viewsets.ModelViewSet):
    queryset = PayCheck.objects.all()
    serializer_class =PayCheckSerializers

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializers

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializers

class BillMonitorViewSet(viewsets.ModelViewSet):
    queryset = BillMonitor.objects.all()
    serializer_class =BillMonitorSerializers

class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = CashFlow.objects.all()
    serializer_class = CashFlowSerializers