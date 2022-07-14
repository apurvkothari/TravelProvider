from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.TripsAPIView.as_view()),
    path('service/<uuid:trip_id>/', views.TripsAPIView.as_view()),
]
