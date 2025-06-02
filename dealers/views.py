from rest_framework import generics, permissions
from .models import Dealer
from .serializers import DealerSerializer
# Create your views here.
class DealerCreateListView(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DealerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]