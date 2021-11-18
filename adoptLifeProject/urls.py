"""adoptLifeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sites.models import Site
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from adoptLifeApp import views
from adoptLifeApp.views import HomeAPI
from adoptLifeApp.views.user_view import DeleteUser, CreateUser, UserList, GetUser, UpdateUser
from adoptLifeApp.views.postViews import PostListCreateView, PostRetrieveUpdateDestroy
from adoptLifeApp.views.pqrsViews import PqrsListCreateView, PqrsRetrieveUpdateDestroy
from adoptLifeApp.views.testimonialViews import TestimonialListCreateView, TestimonialRetrieveUpdateDestroy

urlpatterns = [
    path('', HomeAPI.as_view()),  
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/user/list/', UserList.as_view()),
    path('api/user/create/', CreateUser.as_view()),
    path('api/user/details/<int:pk>/', GetUser.as_view()),
    path('api/user/update/<int:pk>/', UpdateUser.as_view()),
    path('api/user/delete/<int:pk>/', DeleteUser.as_view()),
    path('api/posts/', views.PostListCreateView.as_view()),
    path('api/post/<int:pk>', views.PostRetrieveUpdateDestroy.as_view()),
    path('api/adoptions/', views.AdoptionListCreateView.as_view()),
    path('api/adoption/<int:pk>', views.AdoptionRetrieveUpdateDestroy.as_view()),
    path('api/pqrss/', views.PqrsListCreateView.as_view()),
    path('api/pqrs/<int:pk>', views.PqrsRetrieveUpdateDestroy.as_view()),
    path('api/testimonials/', views.TestimonialListCreateView.as_view()),
    path('api/testimonial/<int:pk>', views.TestimonialRetrieveUpdateDestroy.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.unregister(Site)