from typing import Any

class Hash:
    def __init__(self, native_handle: Any) -> None: ...
    @staticmethod
    def sha1_new() -> Hash: ...
    @staticmethod
    def sha256_new() -> Hash: ...
    @staticmethod
    def md5_new() -> Hash: ...
    def update(self, to_hash: Any) -> None: ...
    def digest(self, truncate_to: int = ...) -> str: ...

class HMAC:
    def __init__(self, native_handle: Any) -> None: ...
    @staticmethod
    def sha256_hmac_new(secret_key: str) -> HMAC: ...
    def update(self, to_hmac: Any) -> None: ...
    def digest(self, truncate_to: int = ...) -> str: ...
