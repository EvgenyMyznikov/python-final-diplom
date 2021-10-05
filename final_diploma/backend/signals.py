from django.dispatch import receiver, Signal
from .models import User
from .tasks import send_email_task


new_order = Signal(
    providing_args=['user_id'],
)

@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    """
    we send a letter when the order status changes
    """
    subject = 'Updating the status of your order'
    message = 'Order has been generated'
    user = User.objects.get(id=user_id)
    email = user.email
    send_email_task.apply_async((subject, message, email), countdown=60)