from django.db import models

# Create your models here.


class Member(models.Model):
    uid = models.CharField(max_length=64, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    time_zone = models.CharField(max_length=128, null=True, blank=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    member = models.ForeignKey(Member, related_name='member_act', on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.name
