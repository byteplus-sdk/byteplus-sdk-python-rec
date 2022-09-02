import json
import logging
import os
import time
import uuid
from datetime import timedelta
from signal import SIGKILL
from typing import Optional

from byteplus_rec.region.region import Region
from byteplus_rec.content.content_client import Client
from byteplus_rec.content.content_client_builder import ClientBuilder
from byteplus_rec.content.constant import STAGE_INCREMENTAL
from byteplus_rec.content.example.mock_helper import mock_users, mock_contents, mock_user_events
from byteplus_rec.content.protocol import WriteResponse, WriteDataRequest, FinishWriteDataRequest, Date
from byteplus_rec_core.exception import BizException
from byteplus_rec_core.http_caller import Config
from byteplus_rec_core.metrics.metrics_option import MetricsCfg
from byteplus_rec_core.option import Option
from byteplus_rec_core.status_helper import is_upload_success

log = logging.getLogger(__name__)

# A unique identity assigned by Bytedance.
PROJECT_ID = "***********"

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
# metrics_config: MetricsCfg = MetricsCfg(enable_metrics=True, enable_metrics_log=True, report_interval_seconds=15)
#
# try:
#     client: Client = ClientBuilder() \
#         .account_id("***********") \
#         .region(Region.SG) \
#         .project_id(PROJECT_ID) \
#         .auth_ak("***********") \
#         .auth_sk("***********") \
#         .keep_alive(True) \
#         .caller_config(caller_config) \
#         .metrics_config(metrics_config) \
#         .build()
# except BizException as clientE:
#     log.error("fail to create byteplus rec client, msg:%s", clientE)

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

DEFAULT_FINISH_TIMEOUT = timedelta(milliseconds=800)

# default logLevel is Warning
logging.basicConfig(level=logging.NOTSET)


def main():
    # Write real-time user data
    write_users_example()

    # Finish write real-time user data
    # finish_write_users_example()

    # Write real-time content data
    write_contents_example()

    # Finish write real-time content data
    # finish_write_contents_example()

    # Write real-time user event data
    write_user_events_example()

    # Finish write real-time user event data
    # finish_write_user_events_example()

    # Write self defined topic data
    # write_others_example()

    # Finish write self defined topic data
    # finish_write_others_example()

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
