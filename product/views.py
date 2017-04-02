from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser


class ProductList(APIView):
    def get(self, request, format=None):
        products=Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request,format=None,headers = {"Content-Type": "application/json"}):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get_object(self,pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        products=self.get_object(pk)
        serializer=ProductSerializer(products)
        return Response(serializer.data)
