MAX_WRITE_COUNT = 2000

# STAGE_TRIAL In this stage, data will be only used to test
STAGE_TRIAL = "pre_sync"

# STAGE_PRODUCTION In this stage, data will be used to train model
STAGE_PRODUCTION = "history_sync"

# STAGE_INCREMENTAL_REALTIME In this stage, data will be used to realtime update model
STAGE_INCREMENTAL_REALTIME = "incremental_sync_streaming"

# STAGE_INCREMENTAL_DAILY In this stage, data will be used to daily update model
STAGE_INCREMENTAL_DAILY = "incremental_sync_daily"
