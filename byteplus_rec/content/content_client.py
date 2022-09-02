import logging

from byteplus_rec.content.protocol import WriteDataRequest, WriteResponse, FinishWriteDataRequest
from byteplus_rec_core.exception import BizException
from byteplus_rec_core.http_client import HTTPClient
from byteplus_rec_core.option import Option
from byteplus_rec.content.constant import _MAX_WRITE_COUNT, _MAX_FINISH_COUNT, TOPIC_USER, TOPIC_CONTENT, \
    TOPIC_USER_EVENT, USER_URI, PRODUCT_URI, USER_EVENT_URI, OTHERS_URI, FINISH_USER_URI, FINISH_PRODUCT_URI, \
    FINISH_USER_EVENT_URI, FINISH_OTHERS_URI
from byteplus_rec_core import utils
from byteplus_rec.content.abstract_client import AbstractClient

log = logging.getLogger(__name__)


class Client(AbstractClient):

    def __init__(self, http_client: HTTPClient, project_id: str):
        self._http_client = http_client
        self._project_id = project_id

    def write_users(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        write_request.topic = TOPIC_USER
        return self._do_write_data(write_request, USER_URI, *opts)

    def finish_write_users(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        finish_request.topic = TOPIC_USER
        return self._do_finish_data(finish_request, FINISH_USER_URI, *opts)

    def write_contents(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        write_request.topic = TOPIC_CONTENT
        return self._do_write_data(write_request, PRODUCT_URI, *opts)

    def finish_write_contents(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        finish_request.topic = TOPIC_CONTENT
        return self._do_finish_data(finish_request, FINISH_PRODUCT_URI, *opts)

    def write_user_events(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        write_request.topic = TOPIC_USER_EVENT
        return self._do_write_data(write_request, USER_EVENT_URI, *opts)

    def finish_write_user_events(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        finish_request.topic = TOPIC_USER_EVENT
        return self._do_finish_data(finish_request, FINISH_USER_EVENT_URI, *opts)

    def write_others(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        return self._do_write_data(write_request, OTHERS_URI, *opts)

    def finish_write_others(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        return self._do_finish_data(finish_request, FINISH_OTHERS_URI, *opts)

    def _do_write_data(self, write_request: WriteDataRequest, path: str, *opts: Option) -> WriteResponse:
        if len(self._project_id) > 0 and len(write_request.project_id) == 0:
            write_request.project_id = self._project_id
        self._check_write_data_request(write_request)
        if len(opts) == 0:
            opts = ()
        response: WriteResponse = WriteResponse()
        self._http_client.do_pb_request(path, write_request, response, *opts)
        log.debug("[ByteplusSDK][WriteData] req:\n %s, rsp:\n %s", write_request, response)
        return response

    @staticmethod
    def _check_write_data_request(request: WriteDataRequest):
        if utils.is_empty_str(request.project_id):
            raise BizException("project id in write request is empty")
        if utils.is_empty_str(request.stage):
            raise BizException("stage in write request is empty")
        if len(request.data) > _MAX_WRITE_COUNT:
            raise BizException("Only can receive max to {} items in one request".format(_MAX_WRITE_COUNT))

    def _do_finish_data(self, finish_request: FinishWriteDataRequest, path: str, *opts: Option) -> WriteResponse:
        if len(self._project_id) > 0 and len(finish_request.project_id) == 0:
            finish_request.project_id = self._project_id
        self._check_finish_data_request(finish_request)
        if len(opts) == 0:
            opts = ()
        response: WriteResponse = WriteResponse()
        self._http_client.do_pb_request(path, finish_request, response, *opts)
        log.debug("[ByteplusSDK][WriteData] req:\n %s, rsp:\n %s", finish_request, response)
        return response

    @staticmethod
    def _check_finish_data_request(request: FinishWriteDataRequest):
        if utils.is_empty_str(request.project_id):
            raise BizException("project id is empty")
        if utils.is_empty_str(request.stage):
            raise BizException("stage is empty")
        if utils.is_empty_str(request.topic):
            raise BizException("topic is empty")
        if len(request.data_dates) > _MAX_FINISH_COUNT:
            raise BizException("Only can receive max to {} items in one request".format(_MAX_FINISH_COUNT))

    def release(self):
        self._http_client.shutdown()