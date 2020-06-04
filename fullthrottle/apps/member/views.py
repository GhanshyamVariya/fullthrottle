import logging

from rest_framework import mixins, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from fullthrottle.apps.member.models import Member
from fullthrottle.apps.member.serializers import MemberSerializer

logger = logging.getLogger('apps')


# Create your views here.
@permission_classes([IsAuthenticated])
class MemberViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = MemberSerializer

    queryset = Member.objects.all()
