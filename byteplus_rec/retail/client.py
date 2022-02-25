import logging

from byteplus_rec.retail.protocol import WriteDataRequest, WriteResponse, PredictRequest, PredictResponse, \
    AckServerImpressionsRequest, AckServerImpressionsResponse
from byteplus_rec_core.exception import BizException
from byteplus_rec_core.http_client import HTTPClient, new_http_client_builder
from byteplus_rec_core.option import Option
from byteplus_rec.retail.constant import _MAX_WRITE_COUNT

log = logging.getLogger(__name__)

_ERR_MSG_TOO_MANY_ITEMS: str = "Only can receive max to {} items in one request".format(_MAX_WRITE_COUNT)

_HTTP_HEADER_SERVER_FROM: str = "Server-From"
_SAAS_FLAG: str = "saas"

_ERR_MSG_FORMAT: str = "{},field can not empty"
_ERR_FIELD_PROJECT_ID: str = "project_id"
_ERR_FIELD_STAGE: str = "stage"
_ERR_FIELD_MODEL_ID: str = "model_id"


class Client(object):

    def __init__(self, http_client: HTTPClient):
        self._http_client = http_client

    def _add_saas_flag(self, opts: tuple) -> tuple:
        return opts + (Option.with_header(_HTTP_HEADER_SERVER_FROM, _SAAS_FLAG),)

    @staticmethod
    def _check_predict_request(project_id: str, model_id: str):
        if project_id != "" or model_id != "":
            return
        empty_params = []
        if project_id == "":
            empty_params.append(_ERR_FIELD_PROJECT_ID)
        if model_id == "":
            empty_params.append(_ERR_FIELD_MODEL_ID)
        raise BizException(_ERR_MSG_FORMAT.format(",".join(empty_params)))

    @staticmethod
    def _check_upload_data_request(project_id: str, stage: str):
        if project_id != "" or stage != "":
            return
        empty_params = []
        if project_id == "":
            empty_params.append(_ERR_FIELD_PROJECT_ID)
        if stage == "":
            empty_params.append(_ERR_FIELD_STAGE)
        raise BizException(_ERR_MSG_FORMAT.format(",".join(empty_params)))

    def _do_write_data(self, write_request: WriteDataRequest, url: str, *opts: Option) -> WriteResponse:
        self._check_upload_data_request(write_request.project_id, write_request.stage)
        if len(opts) == 0:
            opts = ()
        if len(write_request.data) > _MAX_WRITE_COUNT:
            log.warning("[ByteplusSDK][WriteData] item count more than '%d'", _MAX_WRITE_COUNT)
            raise BizException(_ERR_MSG_TOO_MANY_ITEMS)
        opts: tuple = self._add_saas_flag(opts)
        response: WriteResponse = WriteResponse()
        self._http_client.do_pb_request(url, write_request, response, *opts)
        log.debug("[ByteplusSDK][WriteData] rsp:\n %s", response)
        return response

    def write_users(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        return self._do_write_data(write_request, "/RetailSaaS/WriteUsers", *opts)

    def write_products(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        return self._do_write_data(write_request, "/RetailSaaS/WriteProducts", *opts)

    def write_user_events(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        return self._do_write_data(write_request, "/RetailSaaS/WriteUserEvents", *opts)

    def predict(self, predict_request: PredictRequest, *opts: Option) -> PredictResponse:
        self._check_predict_request(predict_request.project_id, predict_request.model_id)
        if len(opts) == 0:
            opts = ()
        opts: tuple = self._add_saas_flag(opts)
        response: PredictResponse = PredictResponse()
        self._http_client.do_pb_request("/RetailSaaS/Predict", predict_request, response, *opts)
        log.debug("[ByteplusSDK][Predict] rsp:\n%s", response)
        return response

    def ack_server_impressions(self, ack_request: AckServerImpressionsRequest,
                               *opts: Option) -> AckServerImpressionsResponse:
        self._check_predict_request(ack_request.project_id, ack_request.model_id)
        if len(opts) == 0:
            opts = ()
        opts: tuple = self._add_saas_flag(opts)
        response: AckServerImpressionsResponse = AckServerImpressionsResponse()
        self._http_client.do_pb_request("/RetailSaaS/AckServerImpressions", ack_request, response, *opts)
        log.debug("[ByteplusSDK][AckImpressions] rsp:\n%s", response)
        return response

    def release(self):
        self._http_client.shutdown()


_BYTEPLUS_AUTH_SERVICE = "byteplus_recommend"


class ClientBuilder(object):
    def __init__(self):
        self._tenant_id = ""
        self._token = ""
        self._auth_ak = ""
        self._auth_sk = ""
        self._schema = ""
        self._hosts = None
        self._region = ""
        self._host_header = ""

    def tenant_id(self, tenant_id: str):
        self._tenant_id = tenant_id
        return self

    def token(self, token: str):
        self._token = token
        return self

    def auth_ak(self, auth_ak: str):
        self._auth_ak = auth_ak
        return self

    def auth_sk(self, auth_sk: str):
        self._auth_sk = auth_sk
        return self

    def schema(self, schema: str):
        self._schema = schema
        return self

    def hosts(self, hosts: list):
        self._hosts = hosts
        return self

    def host_header(self, host_header: str):
        self._host_header = host_header
        return self

    def region(self, region: str):
        self._region = region
        return self

    def build(self) -> Client:
        http_client: HTTPClient = new_http_client_builder() \
            .tenant_id(self._tenant_id) \
            .token(self._token) \
            .ak(self._auth_ak) \
            .sk(self._auth_sk) \
            .schema(self._schema) \
            .hosts(self._hosts) \
            .region(self._region) \
            .host_header(self._host_header) \
            .use_air_auth(False) \
            .auth_service(_BYTEPLUS_AUTH_SERVICE) \
            .build()
        return Client(http_client)
