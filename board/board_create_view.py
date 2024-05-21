from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BoardSerializer

class BoardCreateView(APIView):
    permission_classes = [permissions.AllowAny]  # 인증 없이 접근 허용

    def post(self, request, *args, **kwargs):
        # 필요한 정보를 request.data에서 받아옴
        title = request.data.get('title', None)
        writer = request.data.get('writer', None)
        content = request.data.get('content', None)

        # 받아온 정보로 게시물 생성에 필요한 시리얼라이저 생성
        serializer = BoardSerializer(data={'title': title, 'writer': writer, 'content': content})

        # 시리얼라이저가 유효한지 검사
        if serializer.is_valid():
            # 게시물 저장
            serializer.save()

            # 저장 성공 시 응답
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 유효하지 않을 경우 에러 응답
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
