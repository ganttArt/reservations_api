from rest_framework import generics, viewsets, renderers
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer


class TableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


def reservation_by_date(request, date):
    if request.method == 'GET':
        reservations = Reservation.objects.filter(date=date)
        serializer = ReservationSerializer(reservations, many=True)
        return JsonResponse(serializer.data, safe=False)
