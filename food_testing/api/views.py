from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from .serializers import FoodDataSerializer
from .models import FoodData, FoodItem
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from .permission import Check_API_KEY_Auth
from rest_framework import viewsets
import csv

# Create your views here.
# Create your views here.
class ProjectListView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        """Retrieve a project based on the request API key."""
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = APIKey.objects.get_from_key(key)
        project = Project.objects.get(api_key=api_key)
        return api_key

@api_view(['GET'])
@permission_classes((Check_API_KEY_Auth,))

def viewOnly(request, format=None):
     if request.method=='GET':
        # GET ALL Ongoing FoodDatas 
        Food = FoodItem.objects.filter(id=pk)
        FoodData_serializer = FoodDataSerializer(Food, many=True)
        return JsonResponse(FoodData_serializer.data, safe=False)
    

@csrf_exempt
def AdminSide (request,pk, format=None):
      
    if request.method=='POST':
    # THIS CAN BE USED ON ADMIN SITE TO ADD FoodData INFO
        FoodData_data=JSONParser().parse(request)
        FoodData_serializer = FoodDataSerializer(data=FoodData_data)
        if FoodData_serializer.is_valid():
            FoodData_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    @api_view(['POST'])
    def detect_food_data(request):
        #Name = request.data.get('Name')
        temperature = request.data.get('temperature')
        humidity = request.data.get('humidity')
        methane = request.data.get('methane')
        Quality = request.data.get('Quality')
        
        if temperature is None or humidity is None or methane is None:
            return Response({'error': 'Temperature, humidity, and methane are required parameters.'}, status=400)
        
        if temperature < 5 or temperature > 60:
            quality = 'Non-Edible'
        elif humidity < 20 or humidity > 80:
            quality = 'Non-Edible'
        elif methane > 20:
            quality = 'Non-Edible'
        
        else:
            quality = 'Edible'

        return Response({'quality': quality})
    
    '''elif request.method=='PATCH':
        data= JSONParser().parse(request)
        object = FoodData.objects.get(id=data.get('id')) 
        FoodData_serializer= FoodDataSerializer(object, data=data, partial=True)
        if FoodData_serializer.is_valid():
            FoodData_serializer.save();
        return JsonResponse("UPDATED", safe=False)

    return JsonResponse("FAILED", safe=False)

    elif request.method=='DELETE':
        # DELETE FoodData INFO
         # SELECTING SPECIFIC FoodData BY FoodData BY ID FOR PATCH & DELETE REQUEST
        data= JSONParser().parse(request)
        Data = FoodData.objects.get(id=pk) 
        Data.delete()
        return JsonResponse("DELETED", safe=False)'''
    
    
def export_data(self, request, queryset):
        # Get the data to export
        data = list(queryset.values('humidity', 'methane', 'temperature', 'Quality'))

        # Create a CSV writer
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="my_data.csv"'
        writer = csv.writer(response)

        # Write the CSV header
        writer.writerow(['humidity', 'methane', 'temperature' , 'Quality'])

        # Write the data rows
        for row in data:
            writer.writerow([row['humidity'], row['methane'], row['temperature'] , row ['Quality']])

        # Return the response with appropriate headers to indicate that it should be downloaded as an Excel file
        response['Content-Type'] = 'application/vnd.ms-excel'
        response['Content-Disposition'] = 'attachment; filename="my_data.xls"'
        return response
export_data.short_description = "Export selected data to Excel"
