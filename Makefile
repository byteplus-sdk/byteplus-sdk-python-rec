gen_retail:
	protoc --python_out=byteplus_rec/retail/protocol -I=byteplus_rec/retail/protocol byteplus_saas_retail.proto
