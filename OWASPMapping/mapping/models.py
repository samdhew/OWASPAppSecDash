from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class tbl_OAS_ERRORDETAILS(models.Model):
    detail_id = models.CharField(max_length=12)
    error_id = models.CharField(max_length=3)
    detail_description = models.TextField(max_length=1000)
    cwe_id = models.CharField(max_length=5)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detail_description


class tbl_OAS_ERRORLEVELS(models.Model):
    level_id = models.CharField(max_length=2)
    level_description = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level_description


class tbl_OAS_ERRORTYPES(models.Model):
    error_id = models.CharField(max_length=3)
    error_description = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.error_description


class tbl_OAS_ERRORDETAILLEVELS(models.Model):
    detail_id = models.CharField(max_length=12)
    level_id = models.CharField(max_length=2)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
