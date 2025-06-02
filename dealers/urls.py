from django.urls import path
from .views import (
    DealerCreateListView,
    DealerRetrieveUpdateDestroyView
)

urlpatterns = [
    path('dealers/', DealerCreateListView.as_view(), name='dealer-list'),
    path('dealers/<int:pk>/', DealerRetrieveUpdateDestroyView.as_view(), name='dealer-detail'),
]