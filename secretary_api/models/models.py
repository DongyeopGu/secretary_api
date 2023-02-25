from django.db import models


class UserInfo(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    gender = models.CharField(max_length=80)
    birth = models.DateField()
    state = models.CharField(max_length=80)
    job_position = models.CharField(max_length=80)
    last_login_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class SNSAuthInfo(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.IntegerField()
    uid = models.CharField(max_length=100)
    sns_channel = models.CharField(max_length=30)
    state = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'sns_auth_info'


class MemberInfo(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.IntegerField()
    gender = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    nickname = models.CharField(max_length=80)
    age = models.IntegerField()
    state = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'member_info'


class MeetingInfo(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.IntegerField()
    meeting_type = models.CharField(max_length=80)
    meeting_name = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    meet_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'meeting_info'


class MeetingMemberInfo(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.IntegerField()
    meeting_idx = models.IntegerField()
    member_idx = models.IntegerField()
    state = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'meeting_member_info'
