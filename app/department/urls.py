from rest_framework.routers import DefaultRouter
from .views import DepartmentController
from rest_framework import viewsets

router = DefaultRouter()
router.register('', viewset=DepartmentController, basename='department')
urlpatterns = router.urls
