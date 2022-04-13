from abc import abstractmethod

from byteplus_rec.retail.protocol import WriteDataRequest, WriteResponse, PredictRequest, PredictResponse, \
    AckServerImpressionsRequest, AckServerImpressionsResponse, FinishWriteDataRequest
from byteplus_rec_core.option import Option


class AbstractClient(object):

    @abstractmethod
    def write_users(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Writes at most 2000 users data at a time. Exceeding 2000 in a request results in
        a rejection.Each element of dataList array is a json serialized string of data.
        One can use this to upload new data, or update existing data.
        """
        raise NotImplementedError

    @abstractmethod
    def finish_write_users(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Recording that user data has been written. Mark at most 100 dates at a time
        No need to finish real-time data, the system will automatically finish when entering the next day
        """
        raise NotImplementedError

    @abstractmethod
    def write_products(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Writes at most 2000 products data at a time. Exceeding 2000 in a request results in
        a rejection.Each element of dataList array is a json serialized string of data.
        One can use this to upload new data, or update existing data.
        """
        raise NotImplementedError

    @abstractmethod
    def finish_write_products(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Recording that product data has been written. Mark at most 100 dates at a time
        No need to finish real-time data, the system will automatically finish when entering the next day
        """
        raise NotImplementedError

    @abstractmethod
    def write_user_events(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Writes at most 2000 user events data at a time. Exceeding 2000 in a request results in
        a rejection.Each element of dataList array is a json serialized string of data.
        One can use this to upload new data, or update existing data (by providing all the fields,
        some data type not support update, e.g. user event).
        """
        raise NotImplementedError

    @abstractmethod
    def finish_write_user_events(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Recording that user event data has been written. Mark at most 100 dates at a time
        In general, you need to pass the date list in FinishWriteDataRequest. While if the date list is empty,
        the data of the previous day will be finished by default.
        No need to finish real-time data, the system will automatically finish when entering the next day
        """
        raise NotImplementedError

    @abstractmethod
    def write_others(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Writes at most 2000 data at a time, the topic of these data is set by users
        One can use this to upload new data, or update existing data.
        """
        raise NotImplementedError

    @abstractmethod
    def finish_write_others(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Recording that some data has been written, the topic of these data is set by users.
        Mark at most 100 dates at a time
        No need to finish real-time data, the system will automatically finish when entering the next day
        """
        raise NotImplementedError

    @abstractmethod
    def predict(self, predict_request: PredictRequest, *opts: Option) -> PredictResponse:
        """
        Gets the list of products (ranked).
        The updated user data will take effect in 24 hours.
        The updated product data will take effect in 30 minutes.
        Depending on how (realtime or batch) the UserEvents are sent back, it will
        be fed into the models and take effect after that.
        """
        raise NotImplementedError

    @abstractmethod
    def ack_server_impressions(self, ack_request: AckServerImpressionsRequest,
                               *opts: Option) -> AckServerImpressionsResponse:
        """
        Sends back the actual product list shown to the users based on the
        customized changes from `PredictResponse`.
        example: our Predict call returns the list of items [1, 2, 3, 4].
        Your custom logic have decided that product 3 has been sold out and
        product 10 needs to be inserted before 2 based on some promotion rules,
        the AckServerImpressionsRequest content items should look like
        [
            {id:1, altered_reason: "kept", rank:1},
            {id:10, altered_reason: "inserted", rank:2},
            {id:2, altered_reason: "kept", rank:3},
            {id:4, altered_reason: "kept", rank:4},
            {id:3, altered_reason: "filtered", rank:0},
        ].
        """
        raise NotImplementedError

    @abstractmethod
    def release(self) -> str:
        """
        release resource used by client
        """
        raise NotImplementedError
