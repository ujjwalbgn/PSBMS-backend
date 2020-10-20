from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ExpenseManagement import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'expenses', views.ExpensesViewSet)
router.register(r'reminder', views.ReminderViewSet)
router.register(r'billMonitor', views.BillMonitorViewSet)
router.register(r'payCheck', views.PayCheckViewSet)
router.register(r'cashFlow', views.CashFlowViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]