from rest_framework import serializers

from fullthrottle.apps.member.models import Member, Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('start_time', 'end_time')


class MemberSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(read_only=True, many=True, source='member_act')

    class Meta:
        model = Member
        fields = ('uid', 'name', 'activity', 'time_zone')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        try:
            ret['id'] = ret.pop('uid')
            ret['real_name'] = ret.pop('name')
            ret['tz'] = ret.pop('time_zone')
            ret['activity_periods'] = ret.pop('activity')
        except:
            pass
        return ret
