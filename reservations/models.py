from django.db import models

class Table(models.Model):
    description = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.description


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date) + ' ' + self.table.description
    
    class Meta:
        unique_together = ['table', 'date']
