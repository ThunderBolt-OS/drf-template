from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

# Create your views here.
@api_view(['GET'])
def index(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
        "data" : "Hello World"
    }
    return Response(return_data)