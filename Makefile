gen_retail:
	protoc --python_out=byteplus-rec/retail/protocol -I=byteplus-rec/retail/protocol byteplus_saas_retail.proto
