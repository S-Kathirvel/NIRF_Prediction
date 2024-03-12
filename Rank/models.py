from django.db import models

# Create your models here.
class NIRFPrediction(models.Model):
    tlr = models.FloatField()
    rpc = models.FloatField()
    go = models.FloatField()
    oi = models.FloatField()
    perception = models.FloatField()
    year = models.IntegerField()
    predicted_rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - Predicted Rank: {self.predicted_rank}"