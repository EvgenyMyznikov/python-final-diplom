from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from rest_framework.routers import DefaultRouter
from my_shop_app.views import ShopListView, CategoryListView, ProductInfoView, RegisterAccount, ConfirmAccount, \
    AccountDetails, LoginAccount, BasketView, PartnerUpdate, PartnerState, PartnerOrders, ContactView, OrderView

app_name = 'my_shop_app'

router = DefaultRouter()
router.register(r'shops', ShopListView, basename='shops')
router.register(r'categories', CategoryListView, basename='categories')
router.register(r'products', ProductInfoView, basename='products')

urlpatterns = [
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('basket', BasketView.as_view(), name='basket'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('order', OrderView.as_view(), name='order'),
]

urlpatterns += router.urls
