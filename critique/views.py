from django.shortcuts import render
from .serializers import CritiqueSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Critique

class CritiqueViewset(ModelViewSet):
    queryset = Critique.objects.all()
    serializer_class = CritiqueSerializer
