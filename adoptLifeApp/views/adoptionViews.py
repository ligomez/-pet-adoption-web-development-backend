from rest_framework import generics
from adoptLifeApp.models import Adoption
from adoptLifeApp.serializers import AdoptionSerializer

class AdoptionListCreateView(generics.ListCreateAPIView):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer

class AdoptionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer 