from typing import Optional, List

from byteplus_rec.content.content_client import Client
from byteplus_rec_core.exception import BizException
from byteplus_rec_core.host_availabler_factory import HostAvailablerFactory
from byteplus_rec_core.http_caller import Config
from byteplus_rec_core.http_client import HTTPClient, new_http_client_builder
from byteplus_rec_core.abstract_region import AbstractRegion
from byteplus_rec_core import utils
from byteplus_rec_core.metrics.metrics_option import MetricsCfg

_BYTEPLUS_AUTH_SERVICE = "byteplus_recommend"


class ClientBuilder(object):
    def __init__(self):
        self._tenant_id: Optional[str] = ""
        self._tenant_id: Optional[str] = ""
        self._project_id: Optional[str] = ""
        self._air_auth_token: Optional[str] = ""
        self._auth_ak: Optional[str] = ""
        self._auth_sk: Optional[str] = ""
        self._schema: Optional[str] = ""
        self._hosts: Optional[List[str]] = None
        self._main_host: Optional[str] = None
        self._region: Optional[AbstractRegion] = None
        self._keep_alive: Optional[bool] = False
        self._caller_config: Optional[Config] = None
        self._host_availabler_factory: Optional[HostAvailablerFactory] = None
        self._metrics_cfg: Optional[MetricsCfg] = None

    def account_id(self, account_id: str):
        self._tenant_id = account_id
        return self

    def tenant_id(self, tenant_id: str):
        self._tenant_id = tenant_id
        return self

    def project_id(self, project_id: str):
        self._project_id = project_id
        return self

    def air_auth_token(self, air_auth_token: str):
        self._air_auth_token = air_auth_token
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

    def main_host(self, main_host: str):
        self._main_host = main_host
        return self

    def region(self, region: AbstractRegion):
        self._region = region
        return self

    def keep_alive(self, keep_alive: bool):
        self._keep_alive = keep_alive
        return self

    def caller_config(self, caller_config: Config):
        self._caller_config = caller_config
        return self

    def host_availabler_factory(self, host_availabler_factory: HostAvailablerFactory):
        self._host_availabler_factory = host_availabler_factory
        return self

    def metrics_config(self, metrics_config):
        self._metrics_cfg = metrics_config
        return self

    def build(self) -> Client:
        self._check_required_field()
        http_client: HTTPClient = new_http_client_builder() \
            .tenant_id(self._tenant_id) \
            .project_id(self._project_id) \
            .air_auth_token(self._air_auth_token) \
            .auth_ak(self._auth_ak) \
            .auth_sk(self._auth_sk) \
            .schema(self._schema) \
            .hosts(self._hosts) \
            .main_host(self._main_host) \
            .region(self._region) \
            .use_air_auth(self._is_use_air_auth()) \
            .auth_service(_BYTEPLUS_AUTH_SERVICE) \
            .caller_config(self._caller_config) \
            .host_availabler_factory(self._host_availabler_factory) \
            .metrics_cfg(self._metrics_cfg) \
            .keep_alive(self._keep_alive) \
            .build()
        return Client(http_client, self._project_id)

    def _is_use_air_auth(self) -> bool:
        return utils.is_all_empty_str([self._auth_ak, self._auth_sk]) and utils.none_empty_str([self._air_auth_token])

    def _check_required_field(self):
        if utils.is_empty_str(self._project_id):
            raise BizException("project id is empty")
