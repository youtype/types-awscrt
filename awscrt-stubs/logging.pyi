"""
Type annotations for awscrt.logging module.

Copyright 2026 Vlad Emelianov
"""

from enum import IntEnum

__all__ = ["CRT_LOG_FORMAT", "LogSubject", "init_logging", "log", "set_log_level"]

CRT_LOG_FORMAT: str = ...

class LogSubject(IntEnum):
    """Log subject identifiers for CRT subsystems."""

    # aws-c-common (package ID 0)
    COMMON_GENERAL = 0x000
    COMMON_TASK_SCHEDULER = 0x001

    # aws-c-io (package ID 1)
    IO_GENERAL = 0x400
    IO_EVENT_LOOP = 0x401
    IO_SOCKET = 0x402
    IO_SOCKET_HANDLER = 0x403
    IO_TLS = 0x404
    IO_ALPN = 0x405
    IO_DNS = 0x406
    IO_PKI = 0x407
    IO_CHANNEL = 0x408
    IO_CHANNEL_BOOTSTRAP = 0x409
    IO_FILE_UTILS = 0x40A
    IO_SHARED_LIBRARY = 0x40B

    # aws-c-http (package ID 2)
    HTTP_GENERAL = 0x800
    HTTP_CONNECTION = 0x801
    HTTP_SERVER = 0x802
    HTTP_STREAM = 0x803
    HTTP_CONNECTION_MANAGER = 0x804
    HTTP_WEBSOCKET = 0x805
    HTTP_WEBSOCKET_SETUP = 0x806

    # aws-c-event-stream (package ID 4)
    EVENT_STREAM_GENERAL = 0x1000
    EVENT_STREAM_CHANNEL_HANDLER = 0x1001
    EVENT_STREAM_RPC_SERVER = 0x1002
    EVENT_STREAM_RPC_CLIENT = 0x1003

    # aws-c-mqtt (package ID 5)
    MQTT_GENERAL = 0x1400
    MQTT_CLIENT = 0x1401
    MQTT_TOPIC_TREE = 0x1402

    # aws-c-auth (package ID 6)
    AUTH_GENERAL = 0x1800
    AUTH_PROFILE = 0x1801
    AUTH_CREDENTIALS_PROVIDER = 0x1802
    AUTH_SIGNING = 0x1803

    # aws-c-cal (package ID 7)
    CAL_GENERAL = 0x1C00
    CAL_ECC = 0x1C01
    CAL_HASH = 0x1C02
    CAL_HMAC = 0x1C03
    CAL_DER = 0x1C04
    CAL_LIBCRYPTO_RESOLVE = 0x1C05
    CAL_RSA = 0x1C06
    CAL_ED25519 = 0x1C07

    # aws-c-s3 (package ID 14)
    S3_GENERAL = 0x3800
    S3_CLIENT = 0x3801

    # aws-c-sdkutils (package ID 15)
    SDKUTILS_GENERAL = 0x3C00
    SDKUTILS_PROFILE = 0x3C01
    SDKUTILS_ENDPOINTS_PARSING = 0x3C02
    SDKUTILS_ENDPOINTS_RESOLVE = 0x3C03
    SDKUTILS_ENDPOINTS_GENERAL = 0x3C04
    SDKUTILS_PARTITIONS_PARSING = 0x3C05
    SDKUTILS_ENDPOINTS_REGEX = 0x3C06

def init_logging(level: int = ...) -> None: ...
def set_log_level(level: int) -> None: ...
def log(level: int, subject: LogSubject, message: str) -> None: ...
