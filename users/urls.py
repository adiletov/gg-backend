from django.urls import path
from .views import UserListView, UserUpdateView, UserView, UserDeleteView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/edit/', UserUpdateView.as_view(),  name='edit'),
    path('profile/', UserView.as_view(), name='user-detail'),
    path('profile/delete/', UserDeleteView.as_view(), name='user-delete')
]
