from django.urls import path
from .consumers import MsgCounsumer

ws_urlpatterns = [
    path('ws/messages', MsgCounsumer.as_asgi(), name='messages_list')
]
