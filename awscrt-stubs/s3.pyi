from concurrent.futures import Future
from enum import IntEnum
from threading import Event
from typing import Any, Callable, List, Optional, Tuple

from awscrt import NativeResource as NativeResource
from awscrt.auth import AwsCredentialsProvider as AwsCredentialsProvider
from awscrt.auth import AwsSigningConfig
from awscrt.http import HttpRequest as HttpRequest
from awscrt.io import ClientBootstrap as ClientBootstrap
from awscrt.io import TlsConnectionOptions as TlsConnectionOptions

class S3RequestType(IntEnum):
    DEFAULT: int
    GET_OBJECT: int
    PUT_OBJECT: int

class S3RequestTlsMode(IntEnum):
    ENABLED: int
    DISABLED: int

class S3Client(NativeResource):
    shutdown_event: Event
    def __init__(
        self,
        *,
        bootstrap: Optional[ClientBootstrap],
        region: str,
        tls_mode: Optional[S3RequestTlsMode] = ...,
        signing_config: Optional[AwsSigningConfig] = ...,
        credential_provider: Optional[S3RequestTlsMode] = ...,
        tls_connection_options: Optional[TlsConnectionOptions] = ...,
        part_size: Optional[int] = ...,
        throughput_target_gbps: Optional[float] = ...,
    ) -> None: ...
    def make_request(
        self,
        *,
        request: HttpRequest,
        type: S3RequestType,
        signing_config: Optional[AwsSigningConfig] = ...,
        credential_provider: Optional[AwsCredentialsProvider] = ...,
        recv_filepath: Optional[str] = ...,
        send_filepath: Optional[str] = ...,
        on_headers: Optional[Callable[[int, List[Tuple[str, str]]], None]] = ...,
        on_body: Optional[Callable[[bytes, int], None]] = ...,
        on_done: Optional[
            Callable[
                [Optional[BaseException], Optional[List[Tuple[str, str]]], Optional[bytes]], None
            ]
        ] = ...,
        on_progress: Optional[Callable[[int], None]] = ...,
    ) -> S3Request: ...

class S3Request(NativeResource):
    shutdown_event: Event
    def __init__(
        self,
        *,
        client: S3Client,
        request: HttpRequest,
        type: S3RequestType,
        signing_config: Optional[AwsSigningConfig] = ...,
        credential_provider: Optional[AwsCredentialsProvider] = ...,
        recv_filepath: Optional[str] = ...,
        send_filepath: Optional[str] = ...,
        on_headers: Optional[Callable[[int, List[Tuple[str, str]]], None]] = ...,
        on_body: Optional[Callable[[bytes, int], None]] = ...,
        on_done: Optional[
            Callable[
                [Optional[BaseException], Optional[List[Tuple[str, str]]], Optional[bytes]], None
            ]
        ] = ...,
        on_progress: Optional[Callable[[int], None]] = ...,
        region: Optional[str] = ...,
    ) -> None: ...
    @property
    def finished_future(self) -> Future[Optional[BaseException]]: ...
    def cancel(self) -> None: ...

class _S3ClientCore:
    def __init__(
        self,
        bootstrap: ClientBootstrap,
        credential_provider: Optional[AwsCredentialsProvider] = ...,
        signing_config: Optional[AwsSigningConfig] = ...,
        tls_connection_options: Optional[TlsConnectionOptions] = ...,
    ) -> None: ...

class _S3RequestCore:
    def __init__(
        self,
        request: HttpRequest,
        finish_future: Future[Optional[BaseException]],
        shutdown_event: Event,
        signing_config: Optional[AwsSigningConfig] = ...,
        credential_provider: Optional[AwsCredentialsProvider] = ...,
        on_headers: Optional[Callable[[int, List[Tuple[str, str]]], None]] = ...,
        on_body: Optional[Callable[[bytes, int], None]] = ...,
        on_done: Optional[
            Callable[
                [Optional[BaseException], Optional[List[Tuple[str, str]]], Optional[bytes]], None
            ]
        ] = ...,
        on_progress: Optional[Callable[[int], None]] = ...,
    ) -> None: ...

def create_default_s3_signing_config(
    *, region: str, credential_provider: AwsCredentialsProvider, **kwargs: Any
) -> AwsSigningConfig: ...
