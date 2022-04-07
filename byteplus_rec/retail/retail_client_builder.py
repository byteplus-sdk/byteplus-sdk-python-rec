from typing import Optional, List

from byteplus_rec.retail.retail_client import Client
from byteplus_rec_core.exception import BizException
from byteplus_rec_core.http_client import HTTPClient, new_http_client_builder
from byteplus_rec_core.abstract_region import AbstractRegion
from byteplus_rec_core import utils

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
        self._region: Optional[AbstractRegion] = None

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

    def region(self, region: AbstractRegion):
        self._region = region
        return self

    def build(self) -> Client:
        self._check_required_field()
        http_client: HTTPClient = new_http_client_builder() \
            .tenant_id(self._tenant_id) \
            .air_auth_token(self._air_auth_token) \
            .auth_ak(self._auth_ak) \
            .auth_sk(self._auth_sk) \
            .schema(self._schema) \
            .hosts(self._hosts) \
            .region(self._region) \
            .project_id(self._project_id) \
            .auth_service(_BYTEPLUS_AUTH_SERVICE) \
            .build()
        return Client(http_client, self._project_id)

    def _check_required_field(self):
        if utils.is_empty_str(self._project_id):
            raise BizException("project id is empty")
