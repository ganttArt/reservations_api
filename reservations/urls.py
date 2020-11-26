from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'table', views.TableViewSet)
router.register(r'reservation', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
