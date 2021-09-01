from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, CategoryViewSet, PartnerOrders, PartnerState, PartnerUpdate, ShopViewSet, \
ProductInfoView, BasketView, ContactView, OrderView

router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('shops', ShopViewSet, basename='shops')

urlpatterns = [
    path('partner/update/', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state/', PartnerState.as_view(), name='partner-state'),
    path('partner/orders/', PartnerOrders.as_view(), name='partner-orders'),
    path('users/contact/', ContactView.as_view(), name='user-contact'),
    path('order/', OrderView.as_view(), name='order'),
    path('products/', ProductInfoView.as_view(), name='shops'),
    path('basket/', BasketView.as_view(), name='basket'),
]

urlpatterns += router.urls
