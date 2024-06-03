from django.urls import path, include
from .views import CritiqueViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'critique', CritiqueViewset)

urlpatterns = [
    path('', include(router.urls)),
]
