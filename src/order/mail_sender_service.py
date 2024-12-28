from django.core.mail import send_mail
from django.conf import settings


def send_order_info(recipient, message):
    subject = f"Заказ успешно оформлен"
    message = f"Детали заказа:\n" f"{message}\n\n"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient]

    send_mail(subject, message, email_from, recipient_list)
