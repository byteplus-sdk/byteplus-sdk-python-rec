import logging

from byteplus_rec.retail.protocol import WriteDataRequest, WriteResponse, PredictRequest, PredictResponse, \
    AckServerImpressionsRequest, AckServerImpressionsResponse
from byteplus_rec_core.exception import BizException
from byteplus_rec_core.http_client import HTTPClient
from byteplus_rec_core.option import Option
from byteplus_rec.retail.constant import _MAX_WRITE_COUNT
from byteplus_rec_core import utils
from byteplus_rec.retail.abstract_client import AbstractClient

log = logging.getLogger(__name__)


class Client(AbstractClient):

    def __init__(self, http_client: HTTPClient, project_id: str):
        self._http_client = http_client
        self._project_id = project_id

    def _do_write_data(self, write_request: WriteDataRequest, path: str, *opts: Option) -> WriteResponse:
        if len(self._project_id) > 0 and len(write_request.project_id) == 0:
            write_request.project_id = self._project_id
        self._check_upload_data_request(write_request)
        if len(opts) == 0:
            opts = ()
        if len(write_request.data) > _MAX_WRITE_COUNT:
            log.warning("[ByteplusSDK][WriteData] item count more than '%d'", _MAX_WRITE_COUNT)
            raise BizException("Only can receive max to {} items in one request".format(_MAX_WRITE_COUNT))
        response: WriteResponse = WriteResponse()
        self._http_client.do_pb_request(path, write_request, response, *opts)
        log.debug("[ByteplusSDK][WriteData] rsp:\n %s", response)
        return response

    @staticmethod
    def _check_upload_data_request(request: WriteDataRequest):
        if utils.is_empty_str(request.project_id):
            raise BizException("project id in upload request is empty")
        if utils.is_empty_str(request.stage):
            raise BizException("stage in upload request is empty")

    def write_users(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        return self._do_write_data(write_request, "/RetailSaaS/WriteUsers", *opts)

    def write_products(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        return self._do_write_data(write_request, "/RetailSaaS/WriteProducts", *opts)

    def write_user_events(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        return self._do_write_data(write_request, "/RetailSaaS/WriteUserEvents", *opts)

    def predict(self, predict_request: PredictRequest, *opts: Option) -> PredictResponse:
        if len(self._project_id) > 0 and len(predict_request.project_id) == 0:
            predict_request.project_id = self._project_id
        self._check_predict_request(predict_request)
        if len(opts) == 0:
            opts = ()
        response: PredictResponse = PredictResponse()
        self._http_client.do_pb_request("/RetailSaaS/Predict", predict_request, response, *opts)
        log.debug("[ByteplusSDK][Predict] rsp:\n%s", response)
        return response

    @staticmethod
    def _check_predict_request(request: PredictRequest):
        if utils.is_empty_str(request.project_id):
            raise BizException("project id in predict request is empty")
        if utils.is_empty_str(request.model_id):
            raise BizException("model id in predict request is empty")

    def ack_server_impressions(self, ack_request: AckServerImpressionsRequest,
                               *opts: Option) -> AckServerImpressionsResponse:
        if len(self._project_id) > 0 and len(ack_request.project_id) == 0:
            ack_request.project_id = self._project_id
        self._check_ack_request(ack_request)
        if len(opts) == 0:
            opts = ()
        response: AckServerImpressionsResponse = AckServerImpressionsResponse()
        self._http_client.do_pb_request("/RetailSaaS/AckServerImpressions", ack_request, response, *opts)
        log.debug("[ByteplusSDK][AckImpressions] rsp:\n%s", response)
        return response

    @staticmethod
    def _check_ack_request(request: AckServerImpressionsRequest):
        if utils.is_empty_str(request.project_id):
            raise BizException("project id in ack request is empty")
        if utils.is_empty_str(request.model_id):
            raise BizException("model id in ack request is empty")

    def release(self):
        self._http_client.shutdown()
