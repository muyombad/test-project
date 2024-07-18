# signals.py
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from django.dispatch import receiver
import django_rest_passwordreset.signals
from django.conf import settings

@receiver(django_rest_passwordreset.signals.reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    reset_url = "{}reset-password-confirm/{}".format(
        settings.FRONTEND_URL,
        reset_password_token.key
    )

    email_subject = "Password Reset Request"
    email_plaintext_message = (
        "You requested a password reset. Click the link below to reset your password:\n\n"
        "{}\n\n"
        "If you did not request this password reset, please ignore this email.".format(reset_url)
    )

    email_html_message = (
        "<p>You requested a password reset. Click the link below to reset your password:</p>"
        "<p><a href='{}'>{}</a></p>"
        "<p>If you did not request this password reset, please ignore this email.</p>".format(reset_url, reset_url)
    )

    email = EmailMultiAlternatives(
        subject=email_subject,
        body=email_plaintext_message,
        from_email="info@hoseconsultsugandaltd.com",
        to=[reset_password_token.user.email]
    )
    email.attach_alternative(email_html_message, "text/html")
    email.send()
