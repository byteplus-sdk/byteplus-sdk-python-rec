import json
import logging
import os
import time
import uuid
from datetime import timedelta
from signal import SIGKILL
from typing import Optional

from google.protobuf.message import Message

from byteplus_rec.region.region import Region
from byteplus_rec.retail.retail_client import Client
from byteplus_rec.retail.retail_client_builder import ClientBuilder
from byteplus_rec.retail.constant import STAGE_INCREMENTAL
from byteplus_rec.retail.example.mock_helper import mock_users, mock_products, mock_user_events, \
    mock_device, mock_predict_product
from byteplus_rec.retail.protocol import WriteResponse, WriteDataRequest, FinishWriteDataRequest, PredictRequest, \
    AckServerImpressionsRequest, Date
from byteplus_rec_core import utils
from byteplus_rec_core.exception import BizException, NetException
from byteplus_rec_core.option import Option
from byteplus_rec_core.status_helper import is_upload_success, is_success

log = logging.getLogger(__name__)

# A unique identity assigned by Bytedance.
PROJECT_ID = "***********"

# Unique id for this model.The saas model id that can be used to get rec results from predict api,
# which is need to fill in URL.
MODEL_ID = "***********"

# Required Param:
#       tenant_id
#       region
#       AK
#       SK
# Optional Param:
#       scheme
#       hosts
try:
    client: Client = ClientBuilder() \
        .account_id("***********") \
        .region(Region.SG) \
        .project_id(PROJECT_ID) \
        .auth_ak("***********") \
        .auth_sk("***********") \
        .build()
except BizException as clientE:
    log.error("fail to create byteplus rec client, msg:%s", clientE)

DEFAULT_RETRY_TIMES = 2

DEFAULT_WRITE_TIMEOUT = timedelta(milliseconds=800)

DEFAULT_PREDICT_TIMEOUT = timedelta(milliseconds=800)

DEFAULT_ACK_IMPRESSIONS_TIMEOUT = timedelta(milliseconds=800)

DEFAULT_FINISH_TIMEOUT = timedelta(milliseconds=800)

# default logLevel is Warning
logging.basicConfig(level=logging.NOTSET)


def main():
    # Write real-time user data
    write_users_example()

    # Finish write real-time user data
    # finish_write_users_example()

    # Write real-time product data
    write_products_example()

    # Finish write real-time product data
    # finish_write_products_example()

    # Write real-time user event data
    write_user_events_example()

    # Finish write real-time user event data
    # finish_write_user_events_example()

    # Write self defined topic data
    # write_others_example()

    # Finish write self defined topic data
    # finish_write_others_example()

    # Get recommendation results
    recommend_example()

    time.sleep(5)
    client.release()
    os.kill(os.getpid(), SIGKILL)


def write_users_example():
    # The "WriteXXX" api can transfer max to 2000 items at one request
    request = _build_write_user_request(1)
    opts = _default_opts(DEFAULT_WRITE_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.write_users, request, opts, DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.write_users(request, *opts)
    except BizException as e:
        log.error("write user occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("write user success")
        return
    log.error("write user find fail, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_write_user_request(count: int) -> WriteDataRequest:
    request = WriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    users = mock_users(count)

    user_str_list = [Optional[str]] * len(users)
    for i in range(len(users)):
        user_str_list[i] = json.dumps(users[i])

    request.data.extend(user_str_list)

    # Optional
    # request.extra["extra_info"] = "value"
    return request


def finish_write_users_example():
    # The "FinishXXX" api can mark max to 100 dates at one request
    request = _build_finish_user_request()
    opts = _default_opts(DEFAULT_FINISH_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.finish_write_users, request, opts, DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.finish_write_users(request, *opts)
    except BizException as e:
        log.error("finish user occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("finish user success")
        return
    log.error("finish user find fail, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_finish_user_request() -> WriteDataRequest:
    request = FinishWriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    return request


def write_products_example():
    # The "WriteXXX" api can transfer max to 2000 items at one request
    request = _build_write_product_request(1)
    opts = _default_opts(DEFAULT_WRITE_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.write_products, request, opts, DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.write_products(request, *opts)
    except BizException as e:
        log.error("write product occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("write product success")
        return
    log.error("write product find fail, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_write_product_request(count: int) -> WriteDataRequest:
    request = WriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    products = mock_products(count)
    product_str_list = [Optional[str]] * len(products)
    for i in range(len(products)):
        product_str_list[i] = json.dumps(products[i])

    request.data.extend(product_str_list)

    # Optional
    # request.extra["extra_info"] = "value"
    return request


def finish_write_products_example():
    # The "FinishXXX" api can mark max to 100 dates at one request
    request = _build_finish_product_request()
    opts = _default_opts(DEFAULT_FINISH_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.finish_write_products, request, opts,
        # DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.finish_write_products(request, *opts)
    except BizException as e:
        log.error("finish product occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("finish product success")
        return
    log.error("finish product find fail, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_finish_product_request() -> WriteDataRequest:
    request = FinishWriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    return request


def write_user_events_example():
    # The "WriteXXX" api can transfer max to 2000 items at one request
    request = _build_write_user_event_request(15)
    opts = _default_opts(DEFAULT_WRITE_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.write_user_events, request, opts, DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.write_user_events(request, *opts)
    except BizException as e:
        log.error("write user_event occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("write user_event success")
        return
    log.error("write user event find failure info, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_write_user_event_request(count: int) -> WriteDataRequest:
    request = WriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    user_events = mock_user_events(count)
    user_event_str_list = [Optional[str]] * len(user_events)
    for i in range(len(user_events)):
        user_event_str_list[i] = json.dumps(user_events[i])

    request.data.extend(user_event_str_list)

    # Optional
    # request.extra["extra_info"] = "value"
    return request


def finish_write_user_events_example():
    # The "FinishXXX" api can mark max to 100 dates at one request
    request = _build_finish_user_event_request()
    opts = _default_opts(DEFAULT_FINISH_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.finish_write_user_events(), request, opts,
        # DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.finish_write_user_events(request, *opts)
    except BizException as e:
        log.error("finish user_event occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("finish user_event success")
        return
    log.error("finish user_event find fail, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_finish_user_event_request() -> WriteDataRequest:
    # dates should be passed when finishing others
    date: Date = Date()
    date.year = 2022
    date.month = 3
    date.day = 28
    request: FinishWriteDataRequest = FinishWriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    request.data_dates.extend([date])
    return request


def write_others_example():
    # The "WriteXXX" api can transfer max to 2000 items at one request
    # The `topic` is datatype, which specify the type of data users are going to write.
    # It is temporarily set to "video", the specific value depends on your need.
    topic = "video"
    request = _build_write_others_request(topic)
    opts = _default_opts(DEFAULT_WRITE_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.write_others, request, opts, DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.write_others(request, *opts)
    except BizException as e:
        log.error("write others occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("write others success")
        return
    log.error("write others find failure info, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_write_others_request(topic: str) -> WriteDataRequest:
    data = dict()
    data["field1"] = 1
    data["field2"] = "value2"

    request = WriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    request.topic = topic
    request.data.append(json.dumps(data))
    # Optional
    # request.extra["extra_info"] = "value"

    return request


def finish_write_others_example():
    # The "FinishXXX" api can mark max to 100 dates at one request
    # The `topic` is datatype, which specify the type of data users are going to write.
    # It is temporarily set to "video", the specific value depends on your need.
    topic = "video"
    request = _build_finish_other_request(topic)
    opts = _default_opts(DEFAULT_FINISH_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.finish_write_others, request, opts,
        # DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.finish_write_others(request, *opts)
    except BizException as e:
        log.error("finish others occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("finish others success")
        return
    log.error("finish others find fail, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_finish_other_request(topic: str) -> WriteDataRequest:
    # dates should be passed when finishing others
    date: Date = Date()
    date.year = 2022
    date.month = 3
    date.day = 8
    request: FinishWriteDataRequest = FinishWriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    request.data_dates.extend([date])
    request.topic = topic
    return request


def recommend_example():
    predict_request = _build_predict_request()
    predict_opts = _default_opts(DEFAULT_PREDICT_TIMEOUT)
    try:
        predict_response = client.predict(predict_request, *predict_opts)
    except (NetException, BizException) as e:
        log.error("predict occur error, msg:%s", e)
        return
    if not is_success(predict_response.status.code):
        log.error("predict find failure info, rsp:\n%s", predict_response)
        return
    log.info("predict success")
    # The items, which is eventually shown to user,
    # should send back to Bytedance for deduplication
    altered_products = do_something_with_predict_result(predict_response.value)
    ack_request = _build_ack_impressions_request(predict_response.request_id, predict_request, altered_products)
    ack_opts = _default_opts(DEFAULT_ACK_IMPRESSIONS_TIMEOUT)
    try:
        utils.do_with_retry(client.ack_server_impressions, ack_request, ack_opts, DEFAULT_RETRY_TIMES)
    except Exception as e:
        log.error("[AckServerImpressions] occur error, msg:%s", e)


def _build_predict_request() -> PredictRequest:
    request = PredictRequest()
    request.model_id = MODEL_ID
    request.user_id = "1457789"
    request.size = 20

    scene = request.scene
    scene.offset = 10

    ctx = request.context
    ctx.candidate_products.extend([mock_predict_product()])
    ctx.root_product.CopyFrom(mock_predict_product())
    ctx.device.CopyFrom(mock_device())

    # request.extra["extra_info"] = "extra"
    return request


def do_something_with_predict_result(predict_result):
    # You can handle recommend results here,
    # such as filter, insert other items, sort again, etc.
    # The list of goods finally displayed to user and the filtered goods
    # should be sent back to bytedance for deduplication
    return conv_to_altered_products(predict_result.response_products)


def conv_to_altered_products(product_results):
    if product_results is None or len(product_results) == 0:
        return
    size = len(product_results)
    altered_products = [Optional[AckServerImpressionsRequest.AlteredProduct]] * size
    for i in range(size):
        product_result = product_results[i]
        altered_product = AckServerImpressionsRequest.AlteredProduct()
        altered_product.altered_reason = "kept"
        altered_product.product_id = product_result.product_id
        altered_product.rank = product_result.rank
        altered_products[i] = altered_product
    return altered_products


def _build_ack_impressions_request(predict_request_id: str, predict_request: PredictRequest, altered_products: list):
    request = AckServerImpressionsRequest()
    request.model_id = predict_request.model_id
    request.predict_request_id = predict_request_id
    request.user_id = predict_request.user_id
    scene: Message = request.scene
    scene.CopyFrom(predict_request.scene)
    request.altered_products.extend(altered_products)
    return request


def _default_opts(timeout: timedelta) -> tuple:
    return (
        Option.with_timeout(timeout),
        Option.with_request_id(str(uuid.uuid1())),
        # # Optional. Add a header to a custom header collection.
        # Option.with_http_header("key", "value"),
        # # Optional. Add a query to a custom query collection.
        # Option.with_http_query("key", "value"),
        # # Optional. It is expected that the server will process the data for the maximum time.
        # # If the processing time exceeds this time, the server will return the result immediately,
        # # regardless of whether there is any remaining data that has not been processed.
        # Option.with_server_timeout(timedelta(milliseconds=5000))
    )


if __name__ == '__main__':
    main()
