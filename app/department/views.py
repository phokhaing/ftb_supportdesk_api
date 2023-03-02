from rest_framework import viewsets
from .serializer import DepartmentSerializer
from .models import DepartmentModel


class DepartmentController(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [DjangoObjectPermissions]
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer
