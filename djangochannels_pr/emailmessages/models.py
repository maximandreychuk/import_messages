from django.db import models


class Message(models.Model):
    topic = models.CharField(max_length=500)
    departure_date = models.CharField(max_length=40, default=None)
    received_date = models.CharField(max_length=40, default=None)
    text = models.TextField()


class MessageFile(models.Model):
    file = models.FileField(upload_to='media')
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name='files')
