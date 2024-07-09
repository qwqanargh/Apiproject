from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Shirt
from .serializers import ShirtSerializer


@api_view(["GET", "POST"])
def objects_list(request):
    if request.method == "GET":
        queryset = Shirt.objects.all()
        serializer = ShirtSerializer(queryset, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        serializer = ShirtSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def current_object(request, id):
    qs = Shirt.objects.filter(id=id)

    if not qs.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    cassette = qs.get(id=id)

    if request.method == "GET":
        serializer = ShirtSerializer(cassette)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ShirtSerializer(cassette, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        serializer = ShirtSerializer(cassette, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        cassette.delete()
        return Response(status=status.HTTP_200_OK)
