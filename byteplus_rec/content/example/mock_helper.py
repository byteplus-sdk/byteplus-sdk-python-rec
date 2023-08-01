import json
from typing import Optional

from byteplus_rec.content.protocol import Content, Device


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
        "tags": '["new user","low purchasing power","bargain seeker"]',  # Json Array, use json.dumps()
        "language": "English",
        "subscriber_type": "free",
        "membership_level": "silver",
        "registration_timestamp": 1659958007,
        "country": "USA",
        "province": "Texas",
        "city": "Kirkland",
        "district": "King County",

        # your custom field
        # "custom_field": "custom_value"
    }

    return user


def mock_contents(count: int) -> list:
    contents = [Optional[str]] * count
    for i in range(count):
        content: dict = mock_content()
        content["content_id"] = content["content_id"] + str(i)
        contents[i] = content
    return contents


def mock_content() -> dict:
    content = {
        "content_id": "632461",
        "is_recommendable": 1,
        "categories": '[{"category_depth":1,"category_nodes":[{"id_or_name":"Movie"}]},{"category_depth":2,'
                      '"category_nodes":[{"id_or_name":"Comedy"}]}]',
        "content_type": "video",
        "video_duration": 1200000,
        "content_title": "Green Book Movie Explanation",
        "description": "A brief summary of the main content of the Green Book movie",
        "content_owner_id": "1457789",
        "collection_id": "1342",
        "tags": '["New","Trending"]',
        "image_urls": '["https://images-na.ssl-images-amazon.com/images/I/81WmojBxvbL._AC_UL1500.jpg"]',
        "video_urls": '["https://test_video.mov"]',
        "user_rating": 4.9,
        "current_price": 130.05,
        "original_price": 160.05,
        "publish_timestamp": 1660035734,
        "is_paid_content": True,
        "language": "English",
        "linked_product_id": '["632462","632463"]',
        "source": "self",

        # your custom field
        # "custom_field": "custom_value"
    }

    return content


def mock_user_events(count: int) -> list:
    user_events = [Optional[str]] * count
    for i in range(count):
        user_event: dict = mock_user_event()
        user_events[i] = user_event
    return user_events


def mock_user_event() -> dict:
    user_event = {
        "user_id": "1457787",
        "event_type": "impression",
        "event_timestamp": 1686883465,
        "content_id": "632461",
        "traffic_source": "byteplus",
        "attribution_token": "eyJpc3MiOiJuaW5naGFvLm5ldCIsImV4cCI6IjE0Mzg5NTU0NDUiLCJuYW1lIjoid2FuZ2hhbyIsImFk",
        "scene_name": "Home page",
        "page_number": 2,
        "offset": 10,
        "stay_duration": 150000,
        "parent_content_id": "632431",
        "content_owner_id": "1457789",
        "query": "comedy",
        "platform": "app",
        "os_type": "ios",
        "app_version": "1.0.1",
        "device_model": "iPhone10",
        "os_version": "14.4.2",
        "network": "4g",
        "country": "USA",
        "province": "Texas",
        "city": "Kirkland",
        "district": "King County",
        "purchase_count": 1,
        "paid_price": 100.12,
        "currency": "USD",

        # your custom field
        # "custom_field": "custom_value"
    }

    return user_event


def mock_predict_content() -> Content:
    content = Content()
    content.content_id = "632461"
    return content


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
