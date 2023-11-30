from importlib.metadata import PackageNotFoundError, version

from ._actions import (
    Action,
    AuthAction,
    FinalizeFailed,
    InitFailed,
    SignAction,
    UserAuthData,
    UserSignData,
)
from ._auth import init_auth
from ._cancel import cancel
from ._client import AsyncV60, SyncV60
from ._collect import (
    CompleteCollect,
    CompletionData,
    Device,
    FailedCollect,
    FailedHintCode,
    PendingCollect,
    PendingHintCode,
    TransactionExpired,
    User,
    check,
)
from ._config import config, configure
from ._order import OrderRequest, OrderResponse, Transaction, generate_qr_code
from ._requirement import Requirement
from .errors import BankIDAPIError, BankIDHTTPError
from .typing import OrderRef, PersonalNumber

__all__ = [
    "Action",
    "AuthAction",
    "AsyncV60",
    "BankIDAPIError",
    "BankIDHTTPError",
    "CompleteCollect",
    "CompletionData",
    "Device",
    "FailedCollect",
    "FailedHintCode",
    "FinalizeFailed",
    "InitFailed",
    "OrderRef",
    "OrderRequest",
    "OrderResponse",
    "PendingCollect",
    "PendingHintCode",
    "PersonalNumber",
    "Requirement",
    "SignAction",
    "SyncV60",
    "Transaction",
    "TransactionExpired",
    "User",
    "UserAuthData",
    "UserSignData",
    "cancel",
    "check",
    "config",
    "configure",
    "generate_qr_code",
    "init_auth",
]

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"
