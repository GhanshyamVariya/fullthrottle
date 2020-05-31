from django.core.management.base import BaseCommand

import json

from datetime import datetime
from fullthrottle.apps.member.models import Member, Activity


class Command(BaseCommand):
    help = 'Load data from JSON data file'

    def add_arguments(self, parser):
        parser.add_argument('--path', dest="path", default=None, type=str)

    def handle(self, *args, **options):

        data_file_path = options['path']

        f = open(data_file_path, )

        data = json.load(f)

        for i in data['members']:
            obj, created = Member.objects.get_or_create(uid=i['id'], name=i['real_name'], time_zone=i['tz'])
            if created:
                for j in i['activity_periods']:

                    start_time = datetime.strptime(j['start_time'], '%b %d %Y %I:%M%p')
                    end_time = datetime.strptime(j['end_time'], '%b %d %Y %I:%M%p')

                    Activity.objects.create(
                        member=Member.objects.get(id=obj.id),
                        start_time=start_time,
                        end_time=end_time
                    )

        f.close()
