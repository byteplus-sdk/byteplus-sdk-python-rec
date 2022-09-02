from abc import abstractmethod

from byteplus_rec.content.protocol import WriteDataRequest, WriteResponse, FinishWriteDataRequest
from byteplus_rec_core.option import Option


class AbstractClient(object):

    @abstractmethod
    def write_users(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Writes at most 2000 users data at a time. Exceeding 2000 in a request results in
        a rejection.Each element of dataList array is a json serialized string of data.
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
    def write_contents(self, write_request: WriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Writes at most 2000 contents data at a time. Exceeding 2000 in a request results in
        a rejection.Each element of dataList array is a json serialized string of data.
        One can use this to upload new data, or update existing data.
        """
        raise NotImplementedError

    @abstractmethod
    def finish_write_contents(self, finish_request: FinishWriteDataRequest, *opts: Option) -> WriteResponse:
        """
        Recording that content data has been written. Mark at most 100 dates at a time
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
    def release(self) -> str:
        """
        release resource used by client
        """
        raise NotImplementedError
