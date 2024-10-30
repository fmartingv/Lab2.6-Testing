from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BurroViewSet

router = DefaultRouter()
router.register(r'burros', BurroViewSet, basename='burros') 

urlpatterns = [
    path('', include(router.urls)),
]