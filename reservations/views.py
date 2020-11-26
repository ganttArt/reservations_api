from rest_framework import generics, viewsets
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer


class TableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    # def get(self, request)