from django.urls import path
from .views import (
    CarListCreateView, CarRetrieveUpdateDestroyView,
    BrandListCreateView, ModelListCreateView, VehicleTypeListCreateView
)

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car-detail'),

    path('brands/', BrandListCreateView.as_view(), name='brand-list'),
    path('models/', ModelListCreateView.as_view(), name='model-list'),
    path('vehicle-types/', VehicleTypeListCreateView.as_view(), name='vehicle-type-list'),
]