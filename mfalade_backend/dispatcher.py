from flask_mail import Message

from mfalade_backend.extensions import mail


def send_email(email_context):
	msg = Message(
		"Hey, you've got a new visitor",
		sender="falademayowa240@gmail.com",
		recipients=["falademayowa240@yahoo.com"]
	)
	msg_template = """
		<p>You've got a new message from <b>{messageSender}</b></p>
		<br />
		<b>{messageTitle}</b>
		<hr />
		<p>Message Body:</p>
		<pre>{messageBody}</pre>
		<br />
		<p>Sender's Contact: {senderContact}</p>
	"""
	msg.body = "testing"
	msg.html = msg_template.format(**email_context)

	mail.send(msg)