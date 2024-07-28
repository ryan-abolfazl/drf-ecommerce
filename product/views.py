from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CategoryViewSet(viewsets.ViewSet):
#     # a simple viewset for viewing all categories
#
#     queryset = Category.objects.all()
#
#     def list(self, request):
#         serializer = CategorySerializer(self.queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
