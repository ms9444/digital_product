from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer

from django.shortcuts import render


class CategoryListView(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoseNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializers.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            products = Product.objects.get(pk=pk)
        except Product.DoseNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(products, context={'request': request})
        return Response(serializer.data)


class FileListView(APIView):
    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):
    def get(self, request, pk, product_id):
        try:
            files = File.objects.get(pk=pk, product_id=product_id)
        except File.DoseNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(files, context={'request': request})
        return Response(serializer.data)



