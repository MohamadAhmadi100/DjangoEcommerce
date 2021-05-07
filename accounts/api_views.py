from .serializers import CreateUserSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
