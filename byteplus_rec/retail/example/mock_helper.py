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
        "location_city": "Kirkland",
        "location_country": "USA",
        "location_district_or_area": "King County",
        "location_postcode": "98033",

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
        "category": '[{"category_depth":1,"category_nodes":[{"id_or_name":"Shoes"}]},'
                    '{"category_depth":2,"category_nodes":[{"id_or_name":"Men\'s Shoes"}]}]',  # Json Array
        "brands": "Adidas",
        "is_recommendable": True,
        "title": "adidas Men's Yeezy Boost 350 V2 Grey/Borang/Dgsogr",
        "price_current_price": 49900,
        "price_origin_price": 69900,
        "quality_score": 4.4,
        "tags": '["New Product","Summer Product"]', # Json Array
        "display_cover_multimedia_url": "https://images-na.ssl-images-amazon.com/images/I/81WmojBxvbL._AC_UL1500_.jpg",
        "display_listing_page_display_type": "image",
        "display_listing_page_display_tags": '["best seller","hot sales"]',  # Json Array
        "display_detail_page_display_tags": '["New Product","Summer Product"]',  # Json Array
        "seller_id": "43485",
        "seller_seller_level": "1",
        "seller_seller_rating": 3.5,
        "product_spec_product_group_id": "1356",
        "product_spec_user_rating": 0.25,
        "product_spec_comment_count": 100,
        "product_spec_source": "self",
        "product_spec_publish_timestamp": 1623193487,

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
        "event_type": "purchase",
        "event_timestamp": 1649650452,
        "scene": "product detail page",
        "scene_page_number": 2,
        "scene_offset": 10,
        "product_id": "632461",
        "device_platform": "app",
        "device_os_type": "android",
        "device_app_version": "9.2.0",
        "device_device_model": "huawei-mate30",
        "device_device_brand": "huawei",
        "device_os_version": "10",
        "device_browser_type": "chrome",
        "device_user_agent": "Mozilla/5.0 (Linux; Android 10; TAS-AN00; HMSCore 5.3.0.312)"
                             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser"
                             "/11.0.8.303 Mobile Safari/537.36",
        "device_network": "3g",
        "context_query": "iPad",
        "context_root_product_id": "441356",
        "attribution_token": "eyJpc3MiOiJuaW5naGFvLm5ldCIsImV4cCI6IjE0Mzg5NTU0NDUiLCJuYW"
                             "1lIjoid2FuZ2hhbyIsImFkbWluIjp0cnVlfQ",
        "rec_info": "CiRiMjYyYjM1YS0xOTk1LTQ5YmMtOGNkNS1mZTVmYTczN2FkNDASJAobcmVjZW50X2hvdF9jbGlja3NfcmV0cmlldm"
                    "VyFQAAAAAYDxoKCgNjdHIdog58PBoKCgNjdnIdANK2OCIHMjcyNTgwMg",
        "traffic_source": "self",
        "purchase_count": 20,
        "detail_page_stay_time": 10,  # 10 second

        # your custom field
        # "custom_field": "custom_value"
    }

    return user_event


def mock_predict_product() -> Product:
    product = Product()
    product.product_id = "632461"
    product.is_recommendable = 1
    product.title = "adidas Men's Yeezy Boost 350 V2 Grey/Borang/Dgsogr"
    product.quality_score = 4.4
    product.tags.extend(["New Product", "Summer Product"])

    category1 = product.categories.add()
    category1.category_depth = 1
    category1_node1 = category1.category_nodes.add()
    category1_node1.id_or_name = "Shoes"
    category2 = product.categories.add()
    category2.category_depth = 1
    category2_node1 = category2.category_nodes.add()
    category2_node1.id_or_name = "Men's Shoes"

    brand1 = product.brands.add()
    brand1.brand_depth = 1
    brand1.id_or_name = "Adidas"
    brand2 = product.brands.add()
    brand2.brand_depth = 2
    brand2.id_or_name = "Yeezy"

    price = product.price
    price.current_price = 49900
    price.origin_price = 69900

    display = product.display
    display.detail_page_display_tags.extend(["FreeShipping", "Return in 7 days without any reasons"])
    display.listing_page_display_tags.extend(["best seller", "hot sales"])
    display.listing_page_display_type = "image"
    display.cover_multimedia_url = "https://images-na.ssl-images-amazon.com/images/I/81WmojBxvbL._AC_UL1500_.jpg"

    spec = product.product_spec
    spec.product_group_id = "1356"
    spec.user_rating = 0.25
    spec.comment_count = 100
    spec.source = "self"
    spec.publish_timestamp = 1623193487

    seller = product.seller
    seller.id = "43485"
    seller.seller_level = "1"
    seller.seller_rating = 3.5

    # product.extra["count"] = "20"

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
