from rest_framework import generics
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from app.serializers import * 
from ..models import *
from datetime import datetime


class ProductList(generics.ListAPIView):
    """
    API объектов Product.    
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    # Добавление '__in' позволяет искать все внутренние filters 
    def get(self, request):
        if request.user.is_superuser:
            products = Product.objects.all()
        else:
            products = Product.objects.get(user=self.request.user)

        queryset = ProductSerializer(products, many=True)
        context = {
            'data' : queryset.data
        }
        return Response(context)

class ProductTypeList(generics.ListAPIView):
    """
    API объектов ProductType.    
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductTypeSerializer

    # Добавление '__in' позволяет искать все внутренние filters 
    def get(self, request):
        if request.user.is_superuser:
            products = ProductType.objects.all()
        else:
            products = ProductType.objects.get(user=self.request.user)

        queryset = ProductTypeSerializer(products, many=True)
        context = {
            'data' : queryset.data
        }
        return Response(context)