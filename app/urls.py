from django.urls import path
from app import views

urlpatterns = [
    path("", views.EcomUserAPIView.as_view(), name="ecom_user"),
]
