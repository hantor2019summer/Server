from django.db import models
from django.utils import timezone

class Fine_Dust(models.Model) :
    density = models.FloatField()
    created_date = models.DateTimeField(default = timezone.now())

    def __str__(self) :
        return str(self.density)

class SwitchLog(models.Model) :
    created_date = models.DateTimeField(default = timezone.now())
    state=models.BooleanField()

    def __str__(self) :
        return str(self.state)+str(self.created_date)
