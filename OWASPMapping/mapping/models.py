from django.db import models
from django.contrib.auth.models import User

class tbl_OAS_ERRORDETAILS(models.Model):
    detail_id = models.CharField(max_length=12,primary_key=True)
    error_id = models.CharField(max_length=3)
    detail_description = models.TextField(max_length=1000)
    cwe_id = models.CharField(max_length=5)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    level_1 = models.CharField(max_length=1,default='1')
    level_2 = models.CharField(max_length=1,default='1')
    level_3 = models.CharField(max_length=1,default='1')
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        prop = {
            'detail_id' : self.detail_id,
            'error_id' : self.error_id,
            'detail_description' : self.detail_description,
            'cwe_id' : self.cwe_id,
            'user_id' : self.user_id,
            'level_1' : self.level_1,
            'level_2' : self.level_2,
            'level_3' : self.level_3,
            'date_posted' : self.date_posted,
            'last_modified' : self.last_modified
        }
        return self.detail_id,self.error_id,self.detail_description,self.cwe_id,self.user_id,self.level_1,self.level_2,self.level_3,self.date_posted,self.last_modified


class tbl_OAS_ERRORLEVELS(models.Model):
    level_id = models.CharField(max_length=2,primary_key=True)
    level_description = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level_description


class tbl_OAS_ERRORTYPES(models.Model):
    error_id = models.CharField(max_length=3,primary_key=True)
    error_description = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.error_description

