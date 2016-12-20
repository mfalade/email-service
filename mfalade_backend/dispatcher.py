from flask_mail import Message

from mfalade_backend.extensions import mail
from mfalade_backend.templates import base_template


def send_email(email_context):
	msg = Message(
		"Hey, you've got a new visitor",
		sender="notifier@mayowafalade.com",
		recipients=["falademayowa240@yahoo.com"]
	)
	msg.html = base_template.format(**email_context)

	mail.send(msg)