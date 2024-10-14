from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BurroViewSet

router = DefaultRouter()
router.register(r'burros', BurroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]