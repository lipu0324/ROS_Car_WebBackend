from django.db import models

# Create your models here.
class Air_Quality(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    co2 = models.FloatField()
    tvoc = models.FloatField()
    place = models.CharField(max_length=100)
    def __str__(self):
        return str(self.date)