from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Board

class BoardDeleteAPIView(APIView):
    def delete(self, request, boardId, format=None):
        try:
            board = Board.objects.get(pk=boardId)
            board.delete()
            return Response({'success': 'Board deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Board.DoesNotExist:
            return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
