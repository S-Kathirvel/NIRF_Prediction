# your_app_name/admin.py

from django.contrib import admin
from .models import NIRFPrediction
import joblib  # assuming you are using joblib to load your model


# Register your models here.
@admin.register(NIRFPrediction)
class NIRFPredictionAdmin(admin.ModelAdmin):
    list_display = ['tlr', 'rpc', 'go', 'oi', 'perception', 'year','predicted_rank']
    search_fields = ['tlr', 'rpc', 'go', 'oi', 'perception','year', 'predicted_rank']