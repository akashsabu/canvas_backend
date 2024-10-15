from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

from .serializers import CanvasDataSerializer
from canvas_data.models import CanvasData


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def CanvasDataUpload(request):
    user = request.user
    overwrite_str  = request.data.get("overwrite", "false")
    overwrite = overwrite_str.lower() == "true" 

    print("overwrite:", overwrite)

    if overwrite:
        # Find the existing project by title
        title = request.data.get("title")
        canvas_data = CanvasData.objects.filter(user=user, title=title).first()

        if canvas_data:
            # Update with the new file and title
            serializer = CanvasDataSerializer(canvas_data, data=request.data, context={'request': request}, partial=True)
            if serializer.is_valid():
                updated_instance = serializer.save()  # Save the updated instance
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Project not found for overwrite"}, status=status.HTTP_404_NOT_FOUND)
    else:
        # Handle new project creation
        serializer = CanvasDataSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            new_instance = serializer.save()  # Save the new instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_canvas_data_list(request):
    user = request.user
    canvas_data = CanvasData.objects.filter(user=user)  # Filter canvas data by user
    serializer = CanvasDataSerializer(canvas_data, many=True)  # Serialize the queryset
    return Response(serializer.data)  # Return serialized data as a response