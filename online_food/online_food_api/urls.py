from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('cat', views.CategoryViewSet, basename='cat')

urlpatterns = [ 
]

urlpatterns = urlpatterns + router.urls
