"""
Type annotations for awscrt.crypto module.

Copyright 2024 Vlad Emelianov
"""

from enum import IntEnum
from typing import Any

from awscrt import NativeResource

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

class RSAEncryptionAlgorithm(IntEnum):
    PKCS1_5: int
    OAEP_SHA256: int
    OAEP_SHA512: int

class RSASignatureAlgorithm(IntEnum):
    PKCS1_5_SHA256: int
    PKCS1_5_SHA1: int
    PSS_SHA256: int

class RSA(NativeResource):
    def __init__(self, binding: Any) -> None: ...
    @staticmethod
    def new_private_key_from_pem_data(
        pem_data: str | bytes | bytearray | memoryview,
    ) -> RSA: ...
    @staticmethod
    def new_public_key_from_pem_data(
        pem_data: str | bytes | bytearray | memoryview,
    ) -> RSA: ...
    @staticmethod
    def new_private_key_from_der_data(
        der_data: str | bytes | bytearray | memoryview,
    ) -> RSA: ...
    @staticmethod
    def new_public_key_from_der_data(der_data: bytes | bytearray | memoryview) -> RSA: ...
    def encrypt(
        self,
        encryption_algorithm: RSAEncryptionAlgorithm,
        plaintext: bytes | bytearray | memoryview,
    ) -> bytes: ...
    def decrypt(
        self,
        encryption_algorithm: RSAEncryptionAlgorithm,
        ciphertext: bytes | bytearray | memoryview,
    ) -> bytes: ...
    def sign(
        self,
        signature_algorithm: RSASignatureAlgorithm,
        digest: bytes | bytearray | memoryview,
    ) -> bytes: ...
    def verify(
        self,
        signature_algorithm: RSASignatureAlgorithm,
        digest: bytes | bytearray | memoryview,
        signature: bytes | bytearray | memoryview,
    ) -> bool: ...
