import imaplib
import email
from imap_tools import MailBox, AND
import datetime
from .models import Message


mail_pass = "enmmaquzvaqyqydk"
username = "Privet645@yandex.ru"
imap_server = "imap.yandex.ru"

with MailBox(imap_server).login(username, mail_pass, 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        Message.objects.create(
            topic=msg.subject, text=msg.text, departure_date=msg.date_str)
