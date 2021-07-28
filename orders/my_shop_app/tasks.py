import yaml
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives

from my_shop_app.models import Shop, Category, ProductInfo, Product, Parameter, ProductParameter
from orders.celery import app


@app.task()
def send_mail(title, message, email, *args, **kwargs):
    recipient_list = [email]
    try:
        mail = EmailMultiAlternatives(subject=title, body=message, from_email=EMAIL_HOST_USER, to=recipient_list)
        mail.send()
        return f"Title: {mail.subject}, Message: {mail.body}"
    except Exception as error:
        raise error


@app.task()
def import_products(filename, user_id):
    folder = 'data/'
    with open(folder + filename, 'r') as file:
        data = yaml.safe_load(file)
    shop, _ = Shop.objects.get_or_create(user_id=user_id, defaults={'name': data['shop']})
    for category in data['categories']:
        category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
        category_object.shops.add(shop.id)
        category_object.save()
    ProductInfo.objects.filter(shop_id=shop.id).delete()
    for item in data['goods']:
        product, _ = Product.objects.get_or_create(name=item['name'], category_id=item['category'])
        product_info = ProductInfo.objects.create(product_id=product.id,
                                                  external_id=item['id'],
                                                  model=item['model'],
                                                  price=item['price'],
                                                  price_rrc=item['price_rrc'],
                                                  quantity=item['quantity'],
                                                  shop_id=shop.id)
        for name, value in item['parameters'].items():
            parameter_object, _ = Parameter.objects.get_or_create(name=name)
            ProductParameter.objects.create(product_info_id=product_info.id,
                                            parameter_id=parameter_object.id,
                                            value=value)


