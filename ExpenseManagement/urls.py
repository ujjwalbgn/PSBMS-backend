# from django.shortcuts import render
# from django.http import JsonResponse
#
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from ExpenseManagement import views
#
# urlpatterns = [
#     # path('', views.apiOverview, name="api-overview"),
#     # path('expenses/', views.expensesList, name="expensesList"),
#     # path('expenses/<str:pk>', views.expenseDetails, name="expenseDetails"),
#     # path('reminder/', views.reminderList, name="reminderList"),
#     # path('reminder/<str:pk>', views.reminderDetails, name="reminderDetails"),
#     # path('bill-monitor/', views.billMonitorList, name="reminderList"),
#     # path('bill-monitor/<str:pk>', views.billMonitorDetails, name="billMonitorDetails"),
#
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)




# for implementing class based view sets

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ExpenseManagement import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'PayCheck', views.PayCheckViewSet)
# router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]