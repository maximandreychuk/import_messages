from django.contrib import admin
from .models import Message, MessageFile


admin.site.register(Message)
admin.site.register(MessageFile)
