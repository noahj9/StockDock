from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Docket(models.Model):
    number = models.TextField(max_length=100)
    client = models.TextField()
    rep = models.TextField()
    content = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #auto deletes the docket if the author is deleted
