from django.shortcuts import get_object_or_404
from rest_framework import status, serializers
from rest_framework.response import Response


def ResponseSuccess(data: dict, message=None, status=status.HTTP_201_CREATED):
    return Response(
        {
            "success": True,
            "status": status,
            "message": message,
            "data": data,
        }
    )


def ResponseFail(
    status=status.HTTP_404_NOT_FOUND,
    message="Fail, something went wrong!",
):
    return Response(
        {
            "success": False,
            "status": status,
            "message": message,
            "data": None,
        }
    )
