gen_saas_retail:
	protoc --python_out=byteplus_rec/retail/protocol -I=byteplus_rec/retail/protocol byteplus_saas_retail.proto

gen_saas_content:
	protoc --python_out=byteplus_rec/content/protocol -I=byteplus_rec/content/protocol byteplus_saas_content.proto

