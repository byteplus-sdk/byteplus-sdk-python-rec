# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: byteplus_saas_content.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x62yteplus_saas_content.proto\x12\x1e\x62ytedance.byteplus.rec.content\"8\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0f\n\x07success\x18\x03 \x01(\x08\"0\n\x04\x44\x61te\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\"\x84\x01\n\x16\x46inishWriteDataRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\r\n\x05stage\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\x12\x38\n\ndata_dates\x18\n \x03(\x0b\x32$.bytedance.byteplus.rec.content.Date\"*\n\tDataError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\x82\x01\n\rWriteResponse\x12\x36\n\x06status\x18\x01 \x01(\x0b\x32&.bytedance.byteplus.rec.content.Status\x12\x39\n\x06\x65rrors\x18\x02 \x03(\x0b\x32).bytedance.byteplus.rec.content.DataError\"\xcc\x01\n\x10WriteDataRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\r\n\x05stage\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\n \x03(\t\x12J\n\x05\x65xtra\x18\x64 \x03(\x0b\x32;.bytedance.byteplus.rec.content.WriteDataRequest.ExtraEntry\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb2\x07\n\x07\x43ontent\x12\x12\n\ncontent_id\x18\x01 \x01(\t\x12\x18\n\x10is_recommendable\x18\x02 \x01(\x05\x12\x12\n\ncategories\x18\x03 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x04 \x01(\t\x12\x16\n\x0evideo_duration\x18\x05 \x01(\x05\x12\x15\n\rcontent_title\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x15\n\rcontent_owner\x18\x08 \x01(\t\x12\x1f\n\x17\x63ontent_owner_followers\x18\t \x01(\x05\x12\x1c\n\x14\x63ontent_owner_rating\x18\n \x01(\x02\x12\x1a\n\x12\x63ontent_owner_name\x18\x0b \x01(\t\x12\x15\n\rcollection_id\x18\x0c \x01(\t\x12\x0c\n\x04tags\x18\r \x01(\t\x12\x12\n\ntopic_tags\x18\x0e \x01(\t\x12\x12\n\nimage_urls\x18\x0f \x01(\t\x12\x16\n\x0e\x64\x65tail_pic_num\x18\x10 \x01(\x05\x12\x12\n\nvideo_urls\x18\x11 \x01(\t\x12\x13\n\x0buser_rating\x18\x12 \x01(\x02\x12\x13\n\x0bviews_count\x18\x13 \x01(\x05\x12\x16\n\x0e\x63omments_count\x18\x14 \x01(\x05\x12\x13\n\x0blikes_count\x18\x15 \x01(\x05\x12\x14\n\x0cshares_count\x18\x16 \x01(\x05\x12\x12\n\nsave_count\x18\x17 \x01(\x05\x12\x15\n\rcurrent_price\x18\x18 \x01(\x05\x12\x16\n\x0eoriginal_price\x18\x19 \x01(\x05\x12\x1a\n\x12\x61vailable_location\x18\x1a \x01(\t\x12\x19\n\x11publish_timestamp\x18\x1b \x01(\x05\x12\x18\n\x10update_timestamp\x18\x1c \x01(\x05\x12!\n\x19\x63opyright_start_timestamp\x18\x1d \x01(\x05\x12\x1f\n\x17\x63opyright_end_timestamp\x18\x1e \x01(\x05\x12\x17\n\x0fis_paid_content\x18\x1f \x01(\x08\x12\x10\n\x08language\x18  \x01(\t\x12\x1b\n\x13related_content_ids\x18! \x01(\t\x12\x12\n\nsold_count\x18\" \x01(\x05\x12\x0e\n\x06source\x18# \x01(\t\x12\x41\n\x05\x65xtra\x18\x64 \x03(\x0b\x32\x32.bytedance.byteplus.rec.content.Content.ExtraEntry\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"@\n\x05Scene\x12\x12\n\nscene_name\x18\x01 \x01(\t\x12\x13\n\x0bpage_number\x18\x02 \x01(\x05\x12\x0e\n\x06offset\x18\x03 \x01(\x05\"\xbb\x01\n\x06\x44\x65vice\x12\x10\n\x08platform\x18\x01 \x01(\t\x12\x0f\n\x07os_type\x18\x02 \x01(\t\x12\x13\n\x0b\x61pp_version\x18\x03 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x04 \x01(\t\x12\x14\n\x0c\x64\x65vice_brand\x18\x05 \x01(\t\x12\x12\n\nos_version\x18\x06 \x01(\t\x12\x14\n\x0c\x62rowser_type\x18\x07 \x01(\t\x12\x12\n\nuser_agent\x18\x08 \x01(\t\x12\x0f\n\x07network\x18\t \x01(\t\"\x9c\x04\n\x0ePredictRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\n \x01(\t\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x34\n\x05scene\x18\x0c \x01(\x0b\x32%.bytedance.byteplus.rec.content.Scene\x12O\n\x0f\x63ontent_context\x18\x0e \x01(\x0b\x32\x36.bytedance.byteplus.rec.content.PredictRequest.Context\x12H\n\x05\x65xtra\x18\x64 \x03(\x0b\x32\x39.bytedance.byteplus.rec.content.PredictRequest.ExtraEntry\x1a\xc5\x01\n\x07\x43ontext\x12=\n\x0croot_content\x18\x01 \x01(\x0b\x32\'.bytedance.byteplus.rec.content.Content\x12\x36\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32&.bytedance.byteplus.rec.content.Device\x12\x43\n\x12\x63\x61ndidate_contents\x18\x03 \x03(\x0b\x32\'.bytedance.byteplus.rec.content.Content\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcb\x03\n\rPredictResult\x12X\n\x11response_contents\x18\x01 \x03(\x0b\x32=.bytedance.byteplus.rec.content.PredictResult.ResponseContent\x12G\n\x05\x65xtra\x18\x64 \x03(\x0b\x32\x38.bytedance.byteplus.rec.content.PredictResult.ExtraEntry\x1a\xe8\x01\n\x0fResponseContent\x12\x12\n\ncontent_id\x18\x01 \x01(\t\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x12\x0c\n\x04pctr\x18\x03 \x01(\x01\x12\x0c\n\x04pcvr\x18\x04 \x01(\x01\x12\x10\n\x08rec_info\x18\x05 \x01(\t\x12W\n\x05\x65xtra\x18\x64 \x03(\x0b\x32H.bytedance.byteplus.rec.content.PredictResult.ResponseContent.ExtraEntry\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa3\x01\n\x0fPredictResponse\x12\x36\n\x06status\x18\x01 \x01(\x0b\x32&.bytedance.byteplus.rec.content.Status\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x44\n\rcontent_value\x18\x04 \x01(\x0b\x32-.bytedance.byteplus.rec.content.PredictResult\"\xa3\x05\n\x1b\x41\x63kServerImpressionsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x1a\n\x12predict_request_id\x18\n \x01(\t\x12\x0f\n\x07user_id\x18\x0b \x01(\t\x12\x16\n\x0etraffic_source\x18\x0c \x01(\t\x12\x34\n\x05scene\x18\r \x01(\x0b\x32%.bytedance.byteplus.rec.content.Scene\x12\x64\n\x10\x61ltered_contents\x18\x0f \x03(\x0b\x32J.bytedance.byteplus.rec.content.AckServerImpressionsRequest.AlteredContent\x12U\n\x05\x65xtra\x18\x64 \x03(\x0b\x32\x46.bytedance.byteplus.rec.content.AckServerImpressionsRequest.ExtraEntry\x1a\xf7\x01\n\x0e\x41lteredContent\x12\x12\n\ncontent_id\x18\x01 \x01(\t\x12\x16\n\x0e\x61ltered_reason\x18\x02 \x01(\t\x12\x0c\n\x04rank\x18\x03 \x01(\x05\x12\x17\n\x0f\x63ontent_id_hash\x18\x64 \x01(\x03\x12\x64\n\x05\x65xtra\x18\x65 \x03(\x0b\x32U.bytedance.byteplus.rec.content.AckServerImpressionsRequest.AlteredContent.ExtraEntry\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"V\n\x1c\x41\x63kServerImpressionsResponse\x12\x36\n\x06status\x18\x01 \x01(\x0b\x32&.bytedance.byteplus.rec.content.Status2\xc8\x06\n\x13\x42ytePlusSaasService\x12l\n\tWritUsers\x12\x30.bytedance.byteplus.rec.content.WriteDataRequest\x1a-.bytedance.byteplus.rec.content.WriteResponse\x12o\n\x0cWritContents\x12\x30.bytedance.byteplus.rec.content.WriteDataRequest\x1a-.bytedance.byteplus.rec.content.WriteResponse\x12q\n\x0eWritUserEvents\x12\x30.bytedance.byteplus.rec.content.WriteDataRequest\x1a-.bytedance.byteplus.rec.content.WriteResponse\x12n\n\x0bWriteOthers\x12\x30.bytedance.byteplus.rec.content.WriteDataRequest\x1a-.bytedance.byteplus.rec.content.WriteResponse\x12o\n\x06\x46inish\x12\x36.bytedance.byteplus.rec.content.FinishWriteDataRequest\x1a-.bytedance.byteplus.rec.content.WriteResponse\x12j\n\x07Predict\x12..bytedance.byteplus.rec.content.PredictRequest\x1a/.bytedance.byteplus.rec.content.PredictResponse\x12\x91\x01\n\x14\x41\x63kServerImpressions\x12;.bytedance.byteplus.rec.content.AckServerImpressionsRequest\x1a<.bytedance.byteplus.rec.content.AckServerImpressionsResponseBe\n%com.byteplus.rec.sdk.content.protocolZ<github.com/byteplus-sdk/byteplus-sdk-go-rec/content/protocolb\x06proto3')



_STATUS = DESCRIPTOR.message_types_by_name['Status']
_DATE = DESCRIPTOR.message_types_by_name['Date']
_FINISHWRITEDATAREQUEST = DESCRIPTOR.message_types_by_name['FinishWriteDataRequest']
_DATAERROR = DESCRIPTOR.message_types_by_name['DataError']
_WRITERESPONSE = DESCRIPTOR.message_types_by_name['WriteResponse']
_WRITEDATAREQUEST = DESCRIPTOR.message_types_by_name['WriteDataRequest']
_WRITEDATAREQUEST_EXTRAENTRY = _WRITEDATAREQUEST.nested_types_by_name['ExtraEntry']
_CONTENT = DESCRIPTOR.message_types_by_name['Content']
_CONTENT_EXTRAENTRY = _CONTENT.nested_types_by_name['ExtraEntry']
_SCENE = DESCRIPTOR.message_types_by_name['Scene']
_DEVICE = DESCRIPTOR.message_types_by_name['Device']
_PREDICTREQUEST = DESCRIPTOR.message_types_by_name['PredictRequest']
_PREDICTREQUEST_CONTEXT = _PREDICTREQUEST.nested_types_by_name['Context']
_PREDICTREQUEST_EXTRAENTRY = _PREDICTREQUEST.nested_types_by_name['ExtraEntry']
_PREDICTRESULT = DESCRIPTOR.message_types_by_name['PredictResult']
_PREDICTRESULT_RESPONSECONTENT = _PREDICTRESULT.nested_types_by_name['ResponseContent']
_PREDICTRESULT_RESPONSECONTENT_EXTRAENTRY = _PREDICTRESULT_RESPONSECONTENT.nested_types_by_name['ExtraEntry']
_PREDICTRESULT_EXTRAENTRY = _PREDICTRESULT.nested_types_by_name['ExtraEntry']
_PREDICTRESPONSE = DESCRIPTOR.message_types_by_name['PredictResponse']
_ACKSERVERIMPRESSIONSREQUEST = DESCRIPTOR.message_types_by_name['AckServerImpressionsRequest']
_ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT = _ACKSERVERIMPRESSIONSREQUEST.nested_types_by_name['AlteredContent']
_ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT_EXTRAENTRY = _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT.nested_types_by_name['ExtraEntry']
_ACKSERVERIMPRESSIONSREQUEST_EXTRAENTRY = _ACKSERVERIMPRESSIONSREQUEST.nested_types_by_name['ExtraEntry']
_ACKSERVERIMPRESSIONSRESPONSE = DESCRIPTOR.message_types_by_name['AckServerImpressionsResponse']
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.Status)
  })
_sym_db.RegisterMessage(Status)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.Date)
  })
_sym_db.RegisterMessage(Date)

FinishWriteDataRequest = _reflection.GeneratedProtocolMessageType('FinishWriteDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINISHWRITEDATAREQUEST,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.FinishWriteDataRequest)
  })
_sym_db.RegisterMessage(FinishWriteDataRequest)

DataError = _reflection.GeneratedProtocolMessageType('DataError', (_message.Message,), {
  'DESCRIPTOR' : _DATAERROR,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.DataError)
  })
_sym_db.RegisterMessage(DataError)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESPONSE,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.WriteResponse)
  })
_sym_db.RegisterMessage(WriteResponse)

WriteDataRequest = _reflection.GeneratedProtocolMessageType('WriteDataRequest', (_message.Message,), {

  'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
    'DESCRIPTOR' : _WRITEDATAREQUEST_EXTRAENTRY,
    '__module__' : 'byteplus_saas_content_pb2'
    # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.WriteDataRequest.ExtraEntry)
    })
  ,
  'DESCRIPTOR' : _WRITEDATAREQUEST,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.WriteDataRequest)
  })
_sym_db.RegisterMessage(WriteDataRequest)
_sym_db.RegisterMessage(WriteDataRequest.ExtraEntry)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), {

  'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTENT_EXTRAENTRY,
    '__module__' : 'byteplus_saas_content_pb2'
    # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.Content.ExtraEntry)
    })
  ,
  'DESCRIPTOR' : _CONTENT,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.Content)
  })
_sym_db.RegisterMessage(Content)
_sym_db.RegisterMessage(Content.ExtraEntry)

Scene = _reflection.GeneratedProtocolMessageType('Scene', (_message.Message,), {
  'DESCRIPTOR' : _SCENE,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.Scene)
  })
_sym_db.RegisterMessage(Scene)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.Device)
  })
_sym_db.RegisterMessage(Device)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), {

  'Context' : _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTREQUEST_CONTEXT,
    '__module__' : 'byteplus_saas_content_pb2'
    # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.PredictRequest.Context)
    })
  ,

  'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTREQUEST_EXTRAENTRY,
    '__module__' : 'byteplus_saas_content_pb2'
    # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.PredictRequest.ExtraEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTREQUEST,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.PredictRequest)
  })
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.Context)
_sym_db.RegisterMessage(PredictRequest.ExtraEntry)

PredictResult = _reflection.GeneratedProtocolMessageType('PredictResult', (_message.Message,), {

  'ResponseContent' : _reflection.GeneratedProtocolMessageType('ResponseContent', (_message.Message,), {

    'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
      'DESCRIPTOR' : _PREDICTRESULT_RESPONSECONTENT_EXTRAENTRY,
      '__module__' : 'byteplus_saas_content_pb2'
      # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.PredictResult.ResponseContent.ExtraEntry)
      })
    ,
    'DESCRIPTOR' : _PREDICTRESULT_RESPONSECONTENT,
    '__module__' : 'byteplus_saas_content_pb2'
    # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.PredictResult.ResponseContent)
    })
  ,

  'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTRESULT_EXTRAENTRY,
    '__module__' : 'byteplus_saas_content_pb2'
    # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.PredictResult.ExtraEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTRESULT,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.PredictResult)
  })
_sym_db.RegisterMessage(PredictResult)
_sym_db.RegisterMessage(PredictResult.ResponseContent)
_sym_db.RegisterMessage(PredictResult.ResponseContent.ExtraEntry)
_sym_db.RegisterMessage(PredictResult.ExtraEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTRESPONSE,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.PredictResponse)
  })
_sym_db.RegisterMessage(PredictResponse)

AckServerImpressionsRequest = _reflection.GeneratedProtocolMessageType('AckServerImpressionsRequest', (_message.Message,), {

  'AlteredContent' : _reflection.GeneratedProtocolMessageType('AlteredContent', (_message.Message,), {

    'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
      'DESCRIPTOR' : _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT_EXTRAENTRY,
      '__module__' : 'byteplus_saas_content_pb2'
      # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.AckServerImpressionsRequest.AlteredContent.ExtraEntry)
      })
    ,
    'DESCRIPTOR' : _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT,
    '__module__' : 'byteplus_saas_content_pb2'
    # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.AckServerImpressionsRequest.AlteredContent)
    })
  ,

  'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACKSERVERIMPRESSIONSREQUEST_EXTRAENTRY,
    '__module__' : 'byteplus_saas_content_pb2'
    # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.AckServerImpressionsRequest.ExtraEntry)
    })
  ,
  'DESCRIPTOR' : _ACKSERVERIMPRESSIONSREQUEST,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.AckServerImpressionsRequest)
  })
_sym_db.RegisterMessage(AckServerImpressionsRequest)
_sym_db.RegisterMessage(AckServerImpressionsRequest.AlteredContent)
_sym_db.RegisterMessage(AckServerImpressionsRequest.AlteredContent.ExtraEntry)
_sym_db.RegisterMessage(AckServerImpressionsRequest.ExtraEntry)

AckServerImpressionsResponse = _reflection.GeneratedProtocolMessageType('AckServerImpressionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACKSERVERIMPRESSIONSRESPONSE,
  '__module__' : 'byteplus_saas_content_pb2'
  # @@protoc_insertion_point(class_scope:bytedance.byteplus.rec.content.AckServerImpressionsResponse)
  })
_sym_db.RegisterMessage(AckServerImpressionsResponse)

_BYTEPLUSSAASSERVICE = DESCRIPTOR.services_by_name['BytePlusSaasService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.byteplus.rec.sdk.content.protocolZ<github.com/byteplus-sdk/byteplus-sdk-go-rec/content/protocol'
  _WRITEDATAREQUEST_EXTRAENTRY._options = None
  _WRITEDATAREQUEST_EXTRAENTRY._serialized_options = b'8\001'
  _CONTENT_EXTRAENTRY._options = None
  _CONTENT_EXTRAENTRY._serialized_options = b'8\001'
  _PREDICTREQUEST_EXTRAENTRY._options = None
  _PREDICTREQUEST_EXTRAENTRY._serialized_options = b'8\001'
  _PREDICTRESULT_RESPONSECONTENT_EXTRAENTRY._options = None
  _PREDICTRESULT_RESPONSECONTENT_EXTRAENTRY._serialized_options = b'8\001'
  _PREDICTRESULT_EXTRAENTRY._options = None
  _PREDICTRESULT_EXTRAENTRY._serialized_options = b'8\001'
  _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT_EXTRAENTRY._options = None
  _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT_EXTRAENTRY._serialized_options = b'8\001'
  _ACKSERVERIMPRESSIONSREQUEST_EXTRAENTRY._options = None
  _ACKSERVERIMPRESSIONSREQUEST_EXTRAENTRY._serialized_options = b'8\001'
  _STATUS._serialized_start=63
  _STATUS._serialized_end=119
  _DATE._serialized_start=121
  _DATE._serialized_end=169
  _FINISHWRITEDATAREQUEST._serialized_start=172
  _FINISHWRITEDATAREQUEST._serialized_end=304
  _DATAERROR._serialized_start=306
  _DATAERROR._serialized_end=348
  _WRITERESPONSE._serialized_start=351
  _WRITERESPONSE._serialized_end=481
  _WRITEDATAREQUEST._serialized_start=484
  _WRITEDATAREQUEST._serialized_end=688
  _WRITEDATAREQUEST_EXTRAENTRY._serialized_start=644
  _WRITEDATAREQUEST_EXTRAENTRY._serialized_end=688
  _CONTENT._serialized_start=691
  _CONTENT._serialized_end=1637
  _CONTENT_EXTRAENTRY._serialized_start=644
  _CONTENT_EXTRAENTRY._serialized_end=688
  _SCENE._serialized_start=1639
  _SCENE._serialized_end=1703
  _DEVICE._serialized_start=1706
  _DEVICE._serialized_end=1893
  _PREDICTREQUEST._serialized_start=1896
  _PREDICTREQUEST._serialized_end=2436
  _PREDICTREQUEST_CONTEXT._serialized_start=2193
  _PREDICTREQUEST_CONTEXT._serialized_end=2390
  _PREDICTREQUEST_EXTRAENTRY._serialized_start=644
  _PREDICTREQUEST_EXTRAENTRY._serialized_end=688
  _PREDICTRESULT._serialized_start=2439
  _PREDICTRESULT._serialized_end=2898
  _PREDICTRESULT_RESPONSECONTENT._serialized_start=2620
  _PREDICTRESULT_RESPONSECONTENT._serialized_end=2852
  _PREDICTRESULT_RESPONSECONTENT_EXTRAENTRY._serialized_start=644
  _PREDICTRESULT_RESPONSECONTENT_EXTRAENTRY._serialized_end=688
  _PREDICTRESULT_EXTRAENTRY._serialized_start=644
  _PREDICTRESULT_EXTRAENTRY._serialized_end=688
  _PREDICTRESPONSE._serialized_start=2901
  _PREDICTRESPONSE._serialized_end=3064
  _ACKSERVERIMPRESSIONSREQUEST._serialized_start=3067
  _ACKSERVERIMPRESSIONSREQUEST._serialized_end=3742
  _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT._serialized_start=3449
  _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT._serialized_end=3696
  _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT_EXTRAENTRY._serialized_start=644
  _ACKSERVERIMPRESSIONSREQUEST_ALTEREDCONTENT_EXTRAENTRY._serialized_end=688
  _ACKSERVERIMPRESSIONSREQUEST_EXTRAENTRY._serialized_start=644
  _ACKSERVERIMPRESSIONSREQUEST_EXTRAENTRY._serialized_end=688
  _ACKSERVERIMPRESSIONSRESPONSE._serialized_start=3744
  _ACKSERVERIMPRESSIONSRESPONSE._serialized_end=3830
  _BYTEPLUSSAASSERVICE._serialized_start=3833
  _BYTEPLUSSAASSERVICE._serialized_end=4673
# @@protoc_insertion_point(module_scope)
