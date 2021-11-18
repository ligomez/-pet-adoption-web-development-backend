from django.contrib import admin

from .models.user import User
from .models.post import Post
from .models.adoption import Adoption
from .models.pqrs import Pqrs
from .models.testimonial import Testimonial

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('post_id', 'pet_type', 'pet_gender', 'pet_breed', 'pet_city', 'date', 'active')
    search_fields = ('post_id', 'pet_city', 'pet_breed')
    list_filter = ('pet_type', 'active','pet_gender')

class AdoptionAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('adoption_id', 'user_id', 'post_id', 'date')
    search_fields = ('adoption_id', 'date')
    list_filter = ('date',)

class PqrsAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('pqrs_id', 'title', 'comment', 'date')
    search_fields = ('pqrs_id', 'date')
    list_filter = ('date',)

class TestimonialAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('testimonial_id', 'title', 'comment', 'date')
    search_fields = ('testimonial_id', 'date')
    list_filter = ('date',)



admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(Pqrs, PqrsAdmin)
admin.site.register(Testimonial,TestimonialAdmin)