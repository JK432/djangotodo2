from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
# from django_filters.rest_framework import FilterSet
from django.conf import settings

class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    # filterset_class = ToDoFilterclass

    def get_queryset(self):
        queryset = ToDo.objects.all()
        return queryset