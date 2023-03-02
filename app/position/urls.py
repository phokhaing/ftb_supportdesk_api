from rest_framework.routers import DefaultRouter
from .views import PositionController
from rest_framework import viewsets

router = DefaultRouter()
router.register('', viewset=PositionController, basename='position')
urlpatterns = router.urls
