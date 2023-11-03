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
from byteplus_rec.content.content_client import Client
from byteplus_rec.content.content_client_builder import ClientBuilder
from byteplus_rec.content.constant import STAGE_TRIAL, STAGE_PRODUCTION, STAGE_INCREMENTAL
from byteplus_rec.content.example.mock_helper import mock_users, mock_contents, mock_user_events, mock_predict_content, \
    mock_device
from byteplus_rec.content.protocol import WriteResponse, WriteDataRequest, FinishWriteDataRequest, Date,\
    Scene, PredictRequest, PredictResponse, PredictResult, AckServerImpressionsRequest, AckServerImpressionsResponse
from byteplus_rec_core.exception import BizException, NetException
from byteplus_rec_core.http_caller import Config
from byteplus_rec_core.metrics.metrics_option import MetricsCfg
from byteplus_rec_core.option import Option
from byteplus_rec_core import utils
from byteplus_rec_core.status_helper import is_upload_success, is_success

log = logging.getLogger(__name__)

# A unique identity assigned by Bytedance.
PROJECT_ID = "saas_content_demo"

# Unique id for this model.The saas model id that can be used to get rec results from predict api,
# which is need to fill in URL.
MODEL_ID = "home"

# Required Param:
#       tenant_id
#       region
#       AK
#       SK
# Optional Param:
#       scheme
#       hosts
#       keep_alive
#       caller_config
#       metrics_config

# Full Param Example:
# # Customize the caller config, the parameters in Example are the parameters currently used by default
# # you can customize them according to your own needs.
# # max_idle_connections: the max pool size of request Session.
# # keep_alive_ping_interval_seconds: only takes effect when client.keep_alive(True), heartbeat packet sending interval.
# caller_config: Config = Config(max_idle_connections=32, keep_alive_ping_interval_seconds=45)
# # Metrics configuration, when Metrics and Metrics Log are turned on,
# # the metrics and logs at runtime will be collected and sent to the byteplus server.
# # During debugging, byteplus can help customers troubleshoot problems.
# # enable_metrics: enable metrics, default is false.
# # enable_metrics_log: enable metrics log, default is false.
# # report_interval_seconds:
# #   The time interval for reporting metrics to the byteplus server, the default is 15s.
# #   When the QPS is high, the value of the reporting interval can be reduced to prevent
# #   loss of metrics.
# #   The longest should not exceed 30s, otherwise it will cause the loss of metrics accuracy.
metrics_config: MetricsCfg = MetricsCfg(enable_metrics=True, enable_metrics_log=True, report_interval_seconds=15)
#
# try:
#     client: Client = ClientBuilder() \
#         .account_id("***********") \
#         .region(Region.SG) \
#         .project_id(PROJECT_ID) \
#         .auth_ak("***********") \ # Access Key, used to generate request signature. Saas Standard projects should use.
#         .auth_sk("***********") \ # Secure Key, used to generate request signature. Saas Standard projects should use.
# #         .air_auth_token("***********") \ # The token of this project. Saas Premium projects should use.
#         .keep_alive(True) \
#         .caller_config(caller_config) \
#         .metrics_config(metrics_config) \
#         .build()
# except BizException as clientE:
#     log.error("fail to create byteplus rec client, msg:%s", clientE)

try:
    client: Client = ClientBuilder() \
        .account_id(PROJECT_ID) \
        .region(Region.SG) \
        .project_id(PROJECT_ID) \
        .air_auth_token("***") \
        .main_host("rec-b-ap-singapore-1.byteplusapi.com") \
        .hosts(["rec-b-ap-singapore-1.byteplusapi.com", "rec-ap-singapore-1.byteplusapi.com"]) \
        .metrics_config(metrics_config) \
        .build()
except BizException as clientE:
    log.error("fail to create byteplus rec client, msg:%s", clientE)

DEFAULT_RETRY_TIMES = 2

DEFAULT_WRITE_TIMEOUT = timedelta(milliseconds=800)

DEFAULT_PREDICT_TIMEOUT = timedelta(milliseconds=800)

DEFAULT_ACK_IMPRESSIONS_TIMEOUT = timedelta(milliseconds=800)

DEFAULT_FINISH_TIMEOUT = timedelta(milliseconds=800)

# default logLevel is Warning
logging.basicConfig(level=logging.DEBUG)


def main():
    # Write real-time user data
    # write_users_example()
    #
    # # Finish write real-time user data
    # # finish_write_users_example()
    #
    # # Write real-time content data
    # write_contents_example()
    #
    # # Finish write real-time content data
    # # finish_write_contents_example()
    #
    # # Write real-time user event data
    # write_user_events_example()
    #
    # # Finish write real-time user event data
    # # finish_write_user_events_example()
    #
    # # Write self defined topic data
    # # write_others_example()
    #
    # # Finish write self defined topic data
    # # finish_write_others_example()

    # Get recommendation results
    for i in range(1000):
        recommend_example()
        time.sleep(0.3)

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


def write_contents_example():
    # The "WriteXXX" api can transfer max to 2000 items at one request
    request = _build_write_content_request(1)
    opts = _default_opts(DEFAULT_WRITE_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.write_contents, request, opts, DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.write_contents(request, *opts)
    except BizException as e:
        log.error("write content occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("write content success")
        return
    log.error("write content find fail, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_write_content_request(count: int) -> WriteDataRequest:
    request = WriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    contents = mock_contents(count)
    content_str_list = [Optional[str]] * len(contents)
    for i in range(len(contents)):
        content_str_list[i] = json.dumps(contents[i])

    request.data.extend(content_str_list)

    # Optional
    # request.extra["extra_info"] = "value"
    return request


def finish_write_contents_example():
    # The "FinishXXX" api can mark max to 100 dates at one request
    request = _build_finish_content_request()
    opts = _default_opts(DEFAULT_FINISH_TIMEOUT)
    try:
        # response: WriteResponse = utils.do_with_retry(client.finish_write_contents, request, opts,
        # DEFAULT_RETRY_TIMES)
        response: WriteResponse = client.finish_write_contents(request, *opts)
    except BizException as e:
        log.error("finish content occur err, msg:%s", e)
        return
    if is_upload_success(response.status.code):
        log.info("finish content success")
        return
    log.error("finish content find fail, msg:%s errItems:%s", response.status, response.errors)
    return


def _build_finish_content_request() -> WriteDataRequest:
    request = FinishWriteDataRequest()
    request.stage = STAGE_INCREMENTAL
    return request


def write_user_events_example():
    # The "WriteXXX" api can transfer max to 2000 items at one request
    request = _build_write_user_event_request(1)
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
    date.month = 8
    date.day = 1
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
    # altered_contents = do_something_with_predict_result(predict_response.content_value)
    # ack_request = _build_ack_impressions_request(predict_response.request_id, predict_request, altered_contents)
    # ack_opts = _default_opts(DEFAULT_ACK_IMPRESSIONS_TIMEOUT)
    # try:
    #     utils.do_with_retry(client.ack_server_impressions, ack_request, ack_opts, DEFAULT_RETRY_TIMES)
    # except Exception as e:
    #     log.error("[AckServerImpressions] occur error, msg:%s", e)


def _build_predict_request() -> PredictRequest:
    request = PredictRequest()
    request.model_id = MODEL_ID
    request.user_id = "1457789"
    request.size = 20

    scene = request.scene
    scene.offset = 10

    ctx = request.content_context
    ctx.candidate_contents.extend([mock_predict_content()])
    ctx.root_content.CopyFrom(mock_predict_content())
    ctx.device.CopyFrom(mock_device())

    # request.extra["extra_info"] = "extra"
    return request


def do_something_with_predict_result(predict_result):
    # You can handle recommend results here,
    # such as filter, insert other items, sort again, etc.
    # The list of goods finally displayed to user and the filtered goods
    # should be sent back to bytedance for deduplication
    return conv_to_altered_contents(predict_result.response_contents)


def conv_to_altered_contents(content_results):
    if content_results is None or len(content_results) == 0:
        return
    size = len(content_results)
    altered_contents = [Optional[AckServerImpressionsRequest.AlteredContent]] * size
    for i in range(size):
        content_result = content_results[i]
        altered_content = AckServerImpressionsRequest.AlteredContent()
        altered_content.altered_reason = "kept"
        altered_content.content_id = content_result.content_id
        altered_content.rank = content_result.rank
        altered_contents[i] = altered_content
    return altered_contents


def _build_ack_impressions_request(predict_request_id: str, predict_request: PredictRequest, altered_contents: list):
    request = AckServerImpressionsRequest()
    request.model_id = predict_request.model_id
    request.predict_request_id = predict_request_id
    request.user_id = predict_request.user_id
    # If it is the recommendation result from byteplus, traffic_source is byteplus,
    # if it is the customer's own recommendation result, traffic_source is self.
    request.traffic_source = "byteplus"
    scene: Message = request.scene
    scene.CopyFrom(predict_request.scene)
    request.altered_contents.extend(altered_contents)

    # request.extra["ip"] = "127.0.0.1"
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