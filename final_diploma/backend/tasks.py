from celery.app import shared_task
from orders.celery import app
from django.conf import settings
from django.core.mail import send_mail
import csv
import datetime



@app.task()
def send_email_task(title, message, email, *args, **kwargs):
    '''background task to send an email asynchronously'''
    recipient_list = [email]
    from_email = settings.DEFAULT_FROM_EMAIL
    return send_mail(
        subject=title, 
        message=message, 
        from_email=from_email, 
        recipient_list=recipient_list, 
        fail_silently=False
    )
    # send_mail(subject, message, from_email, recipient_list, 
    # fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
