from django.core.mail import send_mail
from django.conf import settings


class Email:
	
	def post(self, subject, message, to):
		send_mail(
		    subject,
		    message,
		    settings.EMAIL_HOST_USER,
		    [to],
		    fail_silently=False,
		)
