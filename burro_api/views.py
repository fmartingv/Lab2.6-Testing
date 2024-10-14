from rest_framework import viewsets
from .models import Burro
from .serializers import BurroSerializer

class BurroViewSet(viewsets.ModelViewSet):
    queryset = Burro.objects.all()
    serializer_class = BurroSerializer