from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fullthrottle.apps.member.views import MemberViewSet

router = DefaultRouter()
router.register('member-info', MemberViewSet, basename='member')

urlpatterns = [
    path('', include(router.urls)),
]
