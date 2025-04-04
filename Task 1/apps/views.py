from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import AppInfo
from .serializers import AppInfoSerializer

@api_view(['POST'])
def add_app(request):
    serializer = AppInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_app(request, id):
    try:
        app = AppInfo.objects.get(pk=id)
        serializer = AppInfoSerializer(app)
        return Response(serializer.data)
    except AppInfo.DoesNotExist:
        return Response({"error": "App not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_app(request, id):
    try:
        app = AppInfo.objects.get(pk=id)
        app.delete()
        return Response({"message": "App deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except AppInfo.DoesNotExist:
        return Response({"error": "App not found"}, status=status.HTTP_404_NOT_FOUND)
