from rest_framework import viewsets
from .serializer import PositionSerializer
from .models import PositionModel


class PositionController(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [DjangoObjectPermissions]
    queryset = PositionModel.objects.all()
    serializer_class = PositionSerializer
