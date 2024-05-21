from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Board
from .serializers import BoardSerializer

import logging

# Logger 인스턴스 생성
logger = logging.getLogger(__name__)


class BoardCreateView(APIView):
    permission_classes = [permissions.AllowAny]  # 인증 없이 접근 허용

    def post(self, request, *args, **kwargs):
        print(f"Received data from client: %s", request.data)
        # 필요한 정보를 request.data에서 받아옴
        serializer = BoardSerializer(data=request.data)

        # 시리얼라이저가 유효한지 검사
        if serializer.is_valid():
            board = serializer.save()
            print('Serialized board data:', BoardSerializer(board).data)

            return JsonResponse(BoardSerializer(board).data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
