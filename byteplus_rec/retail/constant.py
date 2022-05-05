_MAX_WRITE_COUNT = 2000

_MAX_FINISH_COUNT = 100

# STAGE_TRIAL In this stage, data will be only used to test
STAGE_TRIAL = "trial"

# STAGE_PRODUCTION In this stage, data will be used to train model
STAGE_PRODUCTION = "production"

# STAGE_INCREMENTAL In this stage, data will be used to update model
STAGE_INCREMENTAL = "incremental_sync_streaming"

# STAGE_INCREMENTAL_REALTIME In this stage, data will be used to realtime update model
# Please use `STAGE_INCREMENTAL` instead `STAGE_INCREMENTAL_REALTIME` in most cases
STAGE_INCREMENTAL_REALTIME = "incremental_sync_streaming"

# STAGE_INCREMENTAL_DAILY In this stage, data will be used to daily update model
# Please use `STAGE_INCREMENTAL` instead `STAGE_INCREMENTAL_DAILY` in most cases
STAGE_INCREMENTAL_DAILY = "incremental_sync_daily"

# TOPIC_USER is the type of data when writeUsers or FinishWriteUsers
TOPIC_USER = "user"

# TOPIC_PRODUCT is the type of data when WriteProducts or FinishWriteProducts
TOPIC_PRODUCT = "goods"

# TOPIC_USER_EVENT is the type of data when WriteUserEvents or FinishWriteUserEvents
TOPIC_USER_EVENT = "behavior"

# USER_URI in user topic, url path is end with WriteUsers
USER_URI = "/RetailSaaS/WriteUsers"

# FINISH_USER_URI The URL format of finish information
FINISH_USER_URI = "/RetailSaaS/FinishWriteUsers"

PRODUCT_URI = "/RetailSaaS/WriteProducts"

FINISH_PRODUCT_URI = "/RetailSaaS/FinishWriteProducts"

USER_EVENT_URI = "/RetailSaaS/WriteUserEvents"

FINISH_USER_EVENT_URI = "/RetailSaaS/FinishWriteUserEvents"

OTHERS_URI = "/RetailSaaS/WriteOthers"

FINISH_OTHERS_URI = "/RetailSaaS/FinishWriteOthers"

PREDICT_URI = "/RetailSaaS/Predict"