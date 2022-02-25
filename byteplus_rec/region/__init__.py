from byteplus_rec_core.region import register_region, RegionConfig
from byteplus_rec.region.constant import SG, _SG_HOSTS, _VOLC_CREDENTIAL_SG_REGION

register_region(SG, RegionConfig(_SG_HOSTS, _VOLC_CREDENTIAL_SG_REGION))
