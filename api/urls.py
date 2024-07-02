from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

app_name = 'api'
router.register(r'todo', ToDoViewSet, basename="todo")
urlpatterns = [
    path('', include(router.urls)),
]