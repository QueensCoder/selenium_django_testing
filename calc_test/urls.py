from django.urls import path, include
from .views import send_hi

urlpatterns = [
    path('', send_hi),
]
