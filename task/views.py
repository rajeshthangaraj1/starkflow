from django.shortcuts import render
from django.http import HttpResponse
from task.models import *
from django.contrib.auth.models import User
from .serializers import ConversionSerializer
import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
import os
from dotenv import load_dotenv
load_dotenv()


class ConversionList(generics.ListCreateAPIView):
    queryset = Conversion.objects.all()
    permission_classes = (IsAdminUser,)

    def get(self, request, format=None):
        conversion = Conversion.objects.all()
        serializer_class = ConversionSerializer(conversion, many=True)
        return Response(serializer_class.data)
   
    def post(self, request):
        apikey=os.getenv("APIKEY")
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey='+apikey
        r = requests.get(url)
        data = r.json()
        return Response(data)

def index(request): 

    #User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    return HttpResponse('Using docker compose to create a celery periodic task')


