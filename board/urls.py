from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet

router = DefaultRouter()
router.register(r'board', BoardViewSet)  # Using 'board' instead of 'boards'

urlpatterns = [
    path('', include(router.urls)),
    path('list/', BoardViewSet.as_view({'get': 'list'}), name='board-list'),
]
