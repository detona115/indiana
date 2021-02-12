from django.shortcuts import render

# Create your views here.

from rest_framework import generics, viewsets, permissions
from .models import Parent, Child
from .serializers import ParentSerializer, ChildSerializer

class ParentIdViewSetAPIView(viewsets.ModelViewSet):    
    serializer_class = ParentSerializer
    def get_queryset(self):
        query = self.kwargs['pk']
        if query:
            return Parent.objects.filter(id=self.kwargs['pk'])
        else:
            return Parent.objects.all()

class ParentViewSetAPIView(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
class ChildViewSetAPIView(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ChildIdViewSetAPIView(viewsets.ModelViewSet):
    serializer_class = ChildSerializer
    def get_queryset(self):
        query = self.kwargs['pk']
        if query:
            return Child.objects.filter(id=self.kwargs['pk'])
        else:
            return Child.objects.all()

class ChildrenViewSetAPIView(viewsets.ModelViewSet):
    serializer_class = ChildSerializer
    def get_queryset(self):
        return Child.objects.filter
