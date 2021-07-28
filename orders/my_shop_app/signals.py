from django.dispatch import receiver, Signal
from django_rest_passwordreset.signals import reset_password_token_created
from clients.models import User, ConfirmEmailToken
from my_shop_app.tasks import send_mail

new_user_registered = Signal(
    providing_args=['user_id']
)

new_order = Signal(
    providing_args=['user_id']
)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    """
    Send an email with a password reset token
    """
    title = f"Password Reset Token for {reset_password_token.user}"
    message = f"Token: {reset_password_token.key}"
    email = reset_password_token.user.email
    send_mail(title, message, email)


@receiver(new_user_registered)
def new_user_registered_signal(user_id, **kwargs):
    """
    we send a letter with confirmation of mail
    """
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)
    title = f"Confirmation of registration for {token.user.email}"
    message = f"Token to confirm registration {token.key}"
    email = token.user.email
    send_mail(title, message, email)


@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    """
    we send a letter when the order status changes
    """
    user = User.objects.get(id=user_id)
    title = "Updating order status"
    message = "Order has been generated"
    email = user.email
    send_mail.apply_async(title, message, email, countdown=60)
