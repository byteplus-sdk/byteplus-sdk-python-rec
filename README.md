## byteplus rec python sdk

#### Install the client library
```shell
pip install --upgrade byteplus-rec
```

#### Example
```python
from byteplus_rec.region.region import Region
from byteplus_rec.retail.retail_client import Client
from byteplus_rec.retail.retail_client_builder import ClientBuilder
from byteplus_rec_core.exception import BizException

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

if __name__ == '__main__':
    client.write_users()
    client.predict()
```

#### How to run example
* clone the project.
* install requirements.
* add sdk root path to envs.
* enter the example directory.
* fill necessary parameters.
* run main.py.

```shell
git clone https://github.com/byteplus-sdk/byteplus-sdk-python-rec.git
cd byteplus-sdk-python-rec
pip3 install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$PWD
cd byteplus_rec/retail/example
# fill in projectID, modelID, tenantID, AK, SK and other parameters.
python3 main.py
```

#### For more details
* [code sample](https://docs.byteplus.com/recommend/docs/code-samplesaas)