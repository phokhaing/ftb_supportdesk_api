from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import (
    TokenAuthentication,
    BasicAuthentication,
    SessionAuthentication,
)
from rest_framework.permissions import DjangoObjectPermissions
from .serializer import BranchSerializer
from .models import BranchModel


class BranchController(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [DjangoObjectPermissions]
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer

    # def create(self, request, *args, **kwargs):
    # data = request.data['fname']

    # many = isinstance(data, list)
    # serializer = self.get_serializer(data=data, many=many)
    # serializer.is_valid(raise_exception=True)
    # self.perform_create(serializer)
