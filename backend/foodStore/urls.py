from django.urls import include, path

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'type', TypeViewSet)
router.register(r'side', SideViewSet)
router.register(r'foodorders', FoodOrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
