from typing import Optional

from byteplus_rec.retail.protocol import Device, Product


def mock_users(count: int) -> list:
    users = [Optional[str]] * count
    for i in range(count):
        user: dict = mock_user()
        user["user_id"] = user["user_id"] + str(i)
        users[i] = user
    return users


def mock_user() -> dict:
    user = {
        "user_id": "1457789",
        "gender": "male",
        "age": "23",
        "tags": '["new user","low purchasing power","bargain seeker"]',  # Json Array
        "activation_channel": "AppStore",
        "membership_level": "silver",
        "registration_timestamp": 1623593487,
        "city": "Kirkland",
        "country": "USA",
        "district": "King County",
        "province": "Texas",
        "language": "English"

        # your custom field
        # "custom_field": "custom_value"
    }

    return user


def mock_products(count: int) -> list:
    products = [Optional[str]] * count
    for i in range(count):
        product: dict = mock_product()
        product["product_id"] = product["product_id"] + str(i)
        products[i] = product
    return products


def mock_product() -> dict:
    product = {
        "product_id": "632461",
        "categories": '[{"category_depth":1,"category_nodes":[{"id_or_name":"Shoes"}]},'
                      '{"category_depth":2,"category_nodes":[{"id_or_name":"Mens Shoes"}]}]',  # Json Array
        "brands": "Adidas",
        "is_recommendable": 1,
        "title": "adidas Mens Yeezy Boost 350 V2 Grey/Borang/Dgsogr",
        "current_price": 499.50,
        "original_price": 699.50,
        "tags": '["New Product","Summer Product"]',
        "display_cover_multimedia_url": '["www.demo.jpg"]',  # json array.
        "seller_id": "43485",
        "seller_level": "1",
        "seller_rating": 3.5,
        "product_group_id": "1356",
        "user_rating": 0.25,
        "comment_count": 100,
        "source": "self",
        "publish_timestamp": 1623193487,
        "sold_count": 10

        # your custom field
        # "custom_field": "custom_value"
    }

    return product


def mock_user_events(count: int) -> list:
    user_events = [Optional[str]] * count
    for i in range(count):
        user_event: dict = mock_user_event()
        user_events[i] = user_event
    return user_events


def mock_user_event() -> dict:
    user_event = {
        "user_id": "1457789",
        "event_type": "click",
        "event_timestamp": 1686883465,
        "scene_name": "product detail page",
        "page_number": 2,
        "offset": 10,
        "product_id": "632461",
        "platform": "app",
        "os_type": "android",
        "app_version": "9.2.0",
        "device_model": "huawei-mate30",
        "os_version": "10",
        "network": "3g",
        "query": "iPad",
        "parent_product_id": "441356",
        "attribution_token": "eyJpc3MiOiJuaW5naGFvLm5ldCIsImV4cCI6IjE0Mzg5NTU0NDUiLCJuYW1lIjoid2FuZ2hhbyIsImFkb",
        "traffic_source": "self",
        "purchase_count": 20,
        "paid_price": 100.12,
        "currency": "USD",
        "city": "Kirkland",
        "country": "USA",
        "district": "King County",
        "province": "Texas"

        # your custom field
        # "custom_field": "custom_value"
    }

    return user_event


def mock_predict_product() -> Product:
    product = Product()
    product.product_id = "632461"
    return product


def mock_device() -> Device:
    device = Device()
    device.platform = "app"
    device.os_type = "android"
    device.app_version = "9.2.0"
    device.device_model = "huawei-mate30"
    device.device_brand = "huawei"
    device.os_version = "10"
    device.browser_type = "chrome"
    device.user_agent = "Mozilla/5.0 (Linux; Android 10; TAS-AN00; HMSCore 5.3.0.312) AppleWebKit/537.36 (KHTML, " \
                        "like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.8.303 Mobile Safari/537.36"
    device.network = "3g"
    return device
