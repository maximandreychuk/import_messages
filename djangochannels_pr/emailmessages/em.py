import imaplib
import email
from imap_tools import MailBox, AND
import datetime


def timeStamped(fname, fmt='%Y-%m-%d-%H-%M_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)


mail_pass = "enmmaquzvaqyqydk"
username = "Privet645@yandex.ru"
imap_server = "imap.yandex.ru"

with MailBox(imap_server).login(username, mail_pass, 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        print(f'Дата {msg.date_str}\nТема {msg.subject}\n Текст {msg.text}')
        print('- - - - - - - - - - - -')
        for att in msg.attachments:
            if att.filename:
                with open(timeStamped(att.filename), 'wb') as bin_file:
                    bin_file.write(att.payload)
