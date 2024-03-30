from django.http import JsonResponse
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import numpy as np
#work with heatt disease model in './machine_learning/HeartDiseasePredictionModel.pkl'
import pickle





@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return JsonResponse({'pateints':serializer.data})



@api_view(['POST'])
@csrf_exempt
def patient_create(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        #work with heatt disease model in './machine_learning/HeartDiseasePredictionModel.pkl'
        # Define the path to your saved model file
        model_file_path = 'HeartDiseasePredictionModel.pkl'

        # Load the model from the file
        with open(model_file_path, 'rb') as file:
            loaded_model = pickle.load(file)
            data = serializer.validated_data
            formatted_tuple = convert_to_tuple(data)
             #  change the input data to a numpy array
            input_data_as_numpy_array = np.asarray(formatted_tuple)
        
            # reshape the numpy array as we are predicting for only one instance
            input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
            prediction = loaded_model.predict(input_data_reshaped)
        
        serializer.save()
        return Response({"data": serializer.data, "prediction": prediction[0]}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def convert_to_tuple(data_dict):
    # Define the order of keys according to the desired format
    keys_order = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                  'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    
    # Create a tuple using values from the dictionary in the desired order
    data_tuple = tuple(data_dict[key] for key in keys_order)
    
    return data_tuple

# Example usage:
data_dict = {'age': 52, 'sex': 1, 'cp': 0, 'trestbps': 125, 'chol': 212, 
             'fbs': 0, 'restecg': 1, 'thalach': 168, 'exang': 0, 'oldpeak': 1, 
             'slope': 2, 'ca': 2, 'thal': 3}

formatted_tuple = convert_to_tuple(data_dict)
print(formatted_tuple)
