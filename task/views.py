from django.shortcuts import render
from django.http import HttpResponse
from task.models import *
from .serializers import ConversionSerializer
import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser



class ConversionList(generics.ListCreateAPIView):
    queryset = Conversion.objects.all()

    def get(self, request, format=None):
        conversion = Conversion.objects.all()
        serializer_class = ConversionSerializer(conversion, many=True)
        return Response(serializer_class.data)

    permission_classes = (AllowAny,)
    
    def post(self, request):
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=AN34Z3ELH88WKNYA'
        r = requests.get(url)
        data = r.json()
        return Response(data)

def index(request):   

    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=AN34Z3ELH88WKNYA'
    r = requests.get(url)
    data = r.json()
    if data:
        if data['Realtime Currency Exchange Rate']:
            exchageobjects=data['Realtime Currency Exchange Rate']
            from_currency_code=exchageobjects['1. From_Currency Code']
            from_currency_name=exchageobjects['2. From_Currency Name']
            to_currency_code=exchageobjects['3. To_Currency Code']
            to_currency_name=exchageobjects['4. To_Currency Name']
            exchange_rate=exchageobjects['5. Exchange Rate']
            last_updated_rate=exchageobjects['6. Last Refreshed']

            ## convertor rate create
            conversiondb=Conversion()
            conversiondb.from_currency_code=from_currency_code
            conversiondb.to_currency_code=to_currency_code
            conversiondb.from_currency_name=from_currency_name
            conversiondb.to_currency_name=to_currency_name
            conversiondb.exchange_rate=exchange_rate
            #conversiondb.updated_at=last_updated_rate
            conversiondb.save()
    
    #print(data[0]['From_Currency Name'])
    return HttpResponse("Success")


