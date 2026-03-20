import datetime
from django.db import models
from django.utils import timezone

class Soru(models.Model):
    soru_metni = models.CharField(max_length=250)
    yayinlanma_tarihi = models.DateTimeField("yayınlanma tarihi")

    def __str__(self):
        return self.soru_metni

    def yeni_mi(self):
        return self.yayinlanma_tarihi >= timezone.now() - datetime.timedelta(days=1)

class Secenek(models.Model):
    soru = models.ForeignKey(Soru, on_delete=models.CASCADE)
    secenek_metni = models.CharField(max_length=100)
    dogru_mu = models.BooleanField(default=False)

    def __str__(self):
        return self.secenek_metni