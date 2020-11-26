from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'description', 'capacity']