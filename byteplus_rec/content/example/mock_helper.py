from typing import Optional


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
        "user_id_type": "system_generated",
        "gender": "male",
        "age": "23",
        "tags": '["new user","low purchasing power","bargain seeker"]',  # Json Array, use json.dumps()
        "language": "English",
        "subscriber_type": "free",
        "network": "4g",
        "platform": "app",
        "os_type": "ios",
        "app_version": "1.0.1",
        "device_model": "iPhone10",
        "os_version": "14.4.2",
        "membership_level": "silver",
        "registration_timestamp": 1659958007,
        "update_timestamp": 1659958007,
        "last_login_timestamp": 1659958207,
        "country": "USA",
        "province": "Texas",
        "city": "Kirkland",
        "district": "King County",
        "area": "Neighborhood #1",

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
                      '"category_nodes":[{"id_or_name":"Comedy"}]}]',  # Json Array, use json.dumps()
        "content_type": "video",
        "video_duration": 120000,
        "content_title": "Green Book Movie Explanation",
        "description": "A brief summary of the main content of the Green Book movie",
        "content_owner": "1457789",
        "content_owner_followers": 25,
        "content_owner_rating": 4.5,
        "content_owner_name": "comedy movie commentary",
        "collection_id": "1342",
        "tags": '["New","Trending"]',
        "topic_tags": '["Political","Latest"]',
        "image_urls": '["https://images-na.ssl-images-amazon.com/images/I/81WmojBxvbL._AC_UL1500_.jpg"]',
        "detail_pic_num": 5,
        "video_urls": '["https://test_video.mov"]',
        "user_rating": 4.9,
        "views_count": 10000,
        "comments_count": 100,
        "likes_count": 10,
        "shares_count": 50,
        "save_count": 50,
        "current_price": 1300,
        "original_price": 1600,
        "available_location": '["Cafe 101"]',
        "publish_timestamp": 1660035734,
        "update_timestamp": 1660035734,
        "copyright_start_timestamp": 1660035734,
        "copyright_end_timestamp": 1760035734,
        "is_paid_content": True,
        "language": "English",
        "related_content_ids": '["632462","632463"]',
        "sold_count": 60,
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
        "event_timestamp": 1660036970,
        "content_id": "632461",
        "traffic_source": "byteplus",
        "request_id": "67a9fcf74a82fdc55a26ab4ee12a7b96890407fc0042f8cc014e07a4a560a9ac",
        "rec_info": "CiRiMjYyYjM1YS0xOTk1LTQ5YmMtOGNkNS1mZTVmYTczN2FkNDASJAobcmVjZW50X2hvdF9"
                    "jbGlja3NfcmV0cmlldmVyFQAAAAAYDxoKCgNjdHIdog58PBoKCgNjdnIdANK2OCIHMjcyNTgwMg==",
        "attribution_token": "eyJpc3MiOiJuaW5naGFvLm5ldCIsImV4cCI6IjE0Mzg5NTU0NDUiLCJuY"
                             "W1lIjoid2FuZ2hhbyIsImFkbWluIjp0cnVlfQ",
        "scene_name": "Home page",
        "page_number": 2,
        "offset": 10,
        "play_duration": 150000,
        "video_duration": 1200000,
        "start_time": 150000,
        "end_time": 300000,
        "parent_content_id": "632431",
        "content_owner_id": "1457789",
        "detail_stay_time": 10,
        "dislike_type": "content_id",
        "dislike_value": "675411",
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
        "area": "Neighborhood #1",

        # your custom field
        # "custom_field": "custom_value"
    }

    return user_event