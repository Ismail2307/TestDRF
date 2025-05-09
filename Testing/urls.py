from django.urls import path, include
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]