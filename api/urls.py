from django.urls import path

from .views import TransportList

urlpatterns = [
    path('', TransportList.as_view(), name="transport"),
]