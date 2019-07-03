from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """

    :param order_id:
    :return: mail_sent
    Task to send an email email notification when an order is successfully created
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order number {}'.format(order.id)
    message = 'Dear {}, \n\nYou have successfully placed an order.\
               Your order number is {}'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent
