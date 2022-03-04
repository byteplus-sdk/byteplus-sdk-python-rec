from abc import abstractmethod

from byteplus_rec.retail.protocol import WriteDataRequest, WriteResponse, PredictRequest, PredictResponse, \
    AckServerImpressionsRequest, AckServerImpressionsResponse
from byteplus_rec_core.option import Option


class AbstractClient(object):

    @abstractmethod
    def write_users(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        raise NotImplementedError

    @abstractmethod
    def write_products(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        raise NotImplementedError

    @abstractmethod
    def write_user_events(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        raise NotImplementedError

    @abstractmethod
    def predict(self, predict_request: PredictRequest, *opts: Option) -> PredictResponse:
        raise NotImplementedError

    @abstractmethod
    def ack_server_impressions(self, ack_request: AckServerImpressionsRequest,
                               *opts: Option) -> AckServerImpressionsResponse:
        raise NotImplementedError

    @abstractmethod
    def release(self) -> str:
        raise NotImplementedError
