from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from .views import ShopListView, CategoryListView, ProductInfoView, RegisterAccount, ConfirmAccount, \
    AccountDetails, LoginAccount, BasketView, PartnerUpdate, PartnerState, PartnerOrders, ContactView, OrderView

app_name = 'shop_app'

urlpatterns = [
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('order', OrderView.as_view(), name='order'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('shops', ShopListView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
]