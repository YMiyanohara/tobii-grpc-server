from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EyeTrackerInfo(_message.Message):
    __slots__ = ["eyetracker_model_id"]
    EYETRACKER_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    eyetracker_model_id: str
    def __init__(self, eyetracker_model_id: _Optional[str] = ...) -> None: ...

class GazePosOnScreen(_message.Message):
    __slots__ = ["pos_x", "pos_y"]
    POS_X_FIELD_NUMBER: _ClassVar[int]
    POS_Y_FIELD_NUMBER: _ClassVar[int]
    pos_x: float
    pos_y: float
    def __init__(self, pos_x: _Optional[float] = ..., pos_y: _Optional[float] = ...) -> None: ...
