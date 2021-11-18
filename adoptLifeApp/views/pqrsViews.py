from rest_framework import generics
from adoptLifeApp.models import Pqrs
from adoptLifeApp.serializers import PqrsSerializer

class PqrsListCreateView(generics.ListCreateAPIView):
    queryset = Pqrs.objects.all()
    serializer_class = PqrsSerializer

class PqrsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pqrs.objects.all()
    serializer_class = PqrsSerializer
    