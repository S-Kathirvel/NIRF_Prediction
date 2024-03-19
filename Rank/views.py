from django.shortcuts import render
import joblib
from .models import NIRFPrediction
from django.views import View

def home_view(request):
    return render(request, 'home.html')
    
def predict_view(request):
    if request.method == 'POST':
        default_year = 2024
        print(request.POST)
        
        # input data with default values if key is not present
        input_data = [
            float(request.POST.get('TLR', 0.0)),
            float(request.POST.get('RPC', 0.0)),
            float(request.POST.get('GO', 0.0)),
            float(request.POST.get('OI', 0.0)),
            float(request.POST.get('PERCEPTION', 0.0)),
            int(request.POST.get('Year', default_year)),  # Default to 2023 if 'Year' key is not present
        ]

        # Loading Scaler Model
        scaler_model = joblib.load('Rank/models/Scaler_model.sav')

        # Scale the input data
        input_data_scaled = scaler_model.transform([input_data])

        # Loading the ml model
        model = joblib.load('Rank/models/SVM_model.sav')

        # Make prediction
        prediction = model.predict(input_data_scaled)

        try:
            prediction = int(prediction)
        except (ValueError, TypeError):
            prediction = None

        # Save the prediction to the database
        prediction_instance = NIRFPrediction.objects.create(
            tlr=input_data[0],
            rpc=input_data[1],
            go=input_data[2],
            oi=input_data[3],
            perception=input_data[4],
            predicted_rank=prediction,
            year=input_data[5],  # Assuming 'year' is a field in your NIRFPrediction model
        )

        prediction_instance.save()

        return render(request, 'result.html', {'prediction_instance': prediction_instance})
    
    return render(request, 'predict.html')
