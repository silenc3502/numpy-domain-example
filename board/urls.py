from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .board_create_view import BoardCreateView
from .board_delete_view import BoardDeleteAPIView
from .board_modify_view import BoardModifyAPIView
from .board_read_view import BoardReadAPIView
from .views import BoardViewSet

router = DefaultRouter()
router.register(r'board', BoardViewSet)  # Using 'board' instead of 'boards'

urlpatterns = [
    path('', include(router.urls)),
    path('list/', BoardViewSet.as_view({'get': 'list'}), name='board-list'),
    path('register/', BoardCreateView.as_view(), name='board-register'),
    path('read/<int:boardId>/', BoardReadAPIView.as_view(), name='board-read'),
    path('modify/<int:boardId>/', BoardModifyAPIView.as_view(), name='board-modify'),
    path('delete/<int:boardId>/', BoardDeleteAPIView.as_view(), name='board-delete'),
]
