from typing import List
from byteplus_rec_core.abstract_region import AbstractRegion


class Region(AbstractRegion):
    SG = (["rec-api-sg1.recplusapi.com"], "ap-singapore-1")

    def __init__(self, hosts: List[str], auth_region: str):
        self._hosts = hosts
        self._auth_region = auth_region

    def get_hosts(self) -> List[str]:
        return self._hosts

    def get_auth_region(self) -> str:
        return self._auth_region
