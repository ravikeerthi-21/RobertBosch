from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.conf import settings


class Query(models.Model):
    query = models.CharField(max_length=250, primary_key=True)
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True, editable=False)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="query_submitter", on_delete=models.CASCADE)
    assignedTo = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="query_assignedTo", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.query[:20], self.submitter


class Replies(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    reply = models.CharField(max_length=1000)
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    last_replied_on = models.DateTimeField(auto_now_add=True, editable=False)
    repliedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.query[:20], self.reply[:20], self.repliedBy
