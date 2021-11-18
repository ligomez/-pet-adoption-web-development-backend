from rest_framework import serializers
from adoptLifeApp.models.testimonial import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['testimonial_id', 'title','comment', 'date']
