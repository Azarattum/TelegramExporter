"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
if TYPE_CHECKING:
    from ...tl.types import TypeDataJSON



class AnswerWebhookJSONQueryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe6213f4d
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, query_id, data):
        """
        :param int query_id:
        :param TypeDataJSON data:

        :returns Bool: This type has no constructors.
        """
        self.query_id = query_id  # type: int
        self.data = data  # type: TypeDataJSON

    def to_dict(self):
        return {
            '_': 'AnswerWebhookJSONQueryRequest',
            'query_id': self.query_id,
            'data': self.data.to_dict() if isinstance(self.data, TLObject) else self.data
        }

    def __bytes__(self):
        return b''.join((
            b'M?!\xe6',
            struct.pack('<q', self.query_id),
            bytes(self.data),
        ))

    @classmethod
    def from_reader(cls, reader):
        _query_id = reader.read_long()
        _data = reader.tgread_object()
        return cls(query_id=_query_id, data=_data)


class SendCustomRequestRequest(TLRequest):
    CONSTRUCTOR_ID = 0xaa2769ed
    SUBCLASS_OF_ID = 0xad0352e8

    def __init__(self, custom_method, params):
        """
        :param str custom_method:
        :param TypeDataJSON params:

        :returns DataJSON: Instance of DataJSON.
        """
        self.custom_method = custom_method  # type: str
        self.params = params  # type: TypeDataJSON

    def to_dict(self):
        return {
            '_': 'SendCustomRequestRequest',
            'custom_method': self.custom_method,
            'params': self.params.to_dict() if isinstance(self.params, TLObject) else self.params
        }

    def __bytes__(self):
        return b''.join((
            b"\xedi'\xaa",
            self.serialize_bytes(self.custom_method),
            bytes(self.params),
        ))

    @classmethod
    def from_reader(cls, reader):
        _custom_method = reader.tgread_string()
        _params = reader.tgread_object()
        return cls(custom_method=_custom_method, params=_params)
