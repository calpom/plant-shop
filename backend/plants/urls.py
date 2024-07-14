from django.urls import path, include
from .views import PlantList, PlantDetail

urlpatterns = [
    path('plants/', PlantList.as_view(), name='plant-list'),
    path('plants/<int:pk>/', PlantDetail.as_view(), name='plant-detail'),
]