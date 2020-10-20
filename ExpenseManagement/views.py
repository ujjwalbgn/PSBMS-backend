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
class ReminderViewSet(viewsets.ModelViewSet):
    # here ViewSet.ModelViewSet inherits from djangoREST provide action
    # such as list and create.

    # queryset stores all the objects obtained from the database.
    queryset = Reminder.objects.all()

    # serializer_class is used validating and deserializing input, and for
    # serializing output. ReminderSerializers contains validation information
    serializer_class = ReminderSerializers

class PayCheckViewSet(viewsets.ModelViewSet):
    queryset = PayCheck.objects.all()
    serializer_class =PayCheckSerializers

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializers

class BillMonitorViewSet(viewsets.ModelViewSet):
    queryset = BillMonitor.objects.all()
    serializer_class =BillMonitorSerializers

class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = CashFlow.objects.all()
    serializer_class = CashFlowSerializers