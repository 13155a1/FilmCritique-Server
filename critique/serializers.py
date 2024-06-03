from rest_framework import serializers
from .models import Critique

class CritiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Critique
        fields = '__all__'