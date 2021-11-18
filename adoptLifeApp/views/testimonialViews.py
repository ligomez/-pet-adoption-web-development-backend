from rest_framework import generics
from adoptLifeApp.models import Testimonial
from adoptLifeApp.serializers import TestimonialSerializer

class TestimonialListCreateView(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    