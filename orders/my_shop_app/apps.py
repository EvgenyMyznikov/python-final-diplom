from django.apps import AppConfig


class MyShopAppConfig(AppConfig):
    name = 'my_shop_app'

    def ready(self):
        """
        import signals
        """
        import my_shop_app.signals
