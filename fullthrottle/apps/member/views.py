import logging

from rest_framework import mixins, viewsets

from fullthrottle.apps.member.models import Member
from fullthrottle.apps.member.serializers import MemberSerializer

logger = logging.getLogger('apps')


# Create your views here.
class MemberViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = MemberSerializer

    queryset = Member.objects.all()
