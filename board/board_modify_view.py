from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Board
from .serializers import BoardSerializer


class BoardModifyAPIView(APIView):
    def put(self, request, boardId, format=None):
        try:
            board = Board.objects.get(pk=boardId)
        except Board.DoesNotExist:
            return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
