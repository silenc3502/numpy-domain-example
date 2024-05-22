from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Board
from .serializers import BoardSerializer

class BoardReadAPIView(APIView):
    def get(self, request, boardId, format=None):
        try:
            board = Board.objects.get(pk=boardId)
            serializer = BoardSerializer(board)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Board.DoesNotExist:
            return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)
