"""
Type annotations for awscrt.aio.http module.

Copyright 2025 Vlad Emelianov
"""

import asyncio
from typing import AsyncIterator, Callable

from awscrt.http import (
    Http2Setting,
    HttpClientConnectionBase,
    HttpClientStreamBase,
    HttpProxyOptions,
    HttpRequest,
)
from awscrt.io import ClientBootstrap, SocketOptions, TlsConnectionOptions

class AIOHttpClientConnectionUnified(HttpClientConnectionBase):
    @classmethod
    async def new(
        cls,
        host_name: str,
        port: int,
        bootstrap: ClientBootstrap | None = ...,
        socket_options: SocketOptions | None = ...,
        tls_connection_options: TlsConnectionOptions | None = ...,
        proxy_options: HttpProxyOptions | None = ...,
    ) -> AIOHttpClientConnectionUnified: ...
    async def close(self) -> None: ...
    def request(
        self,
        request: HttpRequest,
        request_body_generator: AsyncIterator[bytes] | None = ...,
        loop: asyncio.AbstractEventLoop | None = ...,
    ) -> AIOHttpClientStreamUnified: ...

class AIOHttpClientConnection(AIOHttpClientConnectionUnified):
    @classmethod
    async def new(
        cls,
        host_name: str,
        port: int,
        bootstrap: ClientBootstrap | None = ...,
        socket_options: SocketOptions | None = ...,
        tls_connection_options: TlsConnectionOptions | None = ...,
        proxy_options: HttpProxyOptions | None = ...,
    ) -> AIOHttpClientConnection: ...
    def request(
        self,
        request: HttpRequest,
        request_body_generator: AsyncIterator[bytes] | None = ...,
        loop: asyncio.AbstractEventLoop | None = ...,
    ) -> AIOHttpClientStream: ...

class AIOHttp2ClientConnection(AIOHttpClientConnectionUnified):
    @classmethod
    async def new(
        cls,
        host_name: str,
        port: int,
        bootstrap: ClientBootstrap | None = ...,
        socket_options: SocketOptions | None = ...,
        tls_connection_options: TlsConnectionOptions | None = ...,
        proxy_options: HttpProxyOptions | None = ...,
        initial_settings: list[Http2Setting] | None = ...,
        on_remote_settings_changed: Callable[[list[Http2Setting]], None] | None = ...,
    ) -> AIOHttp2ClientConnection: ...
    def request(
        self,
        request: HttpRequest,
        request_body_generator: AsyncIterator[bytes] | None = ...,
        loop: asyncio.AbstractEventLoop | None = ...,
    ) -> AIOHttp2ClientStream: ...

class AIOHttpClientStreamUnified(HttpClientStreamBase):
    def __init__(
        self,
        connection: AIOHttpClientConnection,
        request: HttpRequest,
        request_body_generator: AsyncIterator[bytes] | None = ...,
        loop: asyncio.AbstractEventLoop | None = ...,
    ) -> None: ...
    async def get_response_status_code(self) -> int: ...
    async def get_response_headers(self) -> list[tuple[str, str]]: ...
    async def get_next_response_chunk(self) -> bytes: ...
    async def wait_for_completion(self) -> int: ...

class AIOHttpClientStream(AIOHttpClientStreamUnified):
    def __init__(
        self,
        connection: AIOHttpClientConnection,
        request: HttpRequest,
        loop: asyncio.AbstractEventLoop | None = ...,
    ) -> None: ...

class AIOHttp2ClientStream(AIOHttpClientStreamUnified):
    def __init__(
        self,
        connection: AIOHttpClientConnection,
        request: HttpRequest,
        request_body_generator: AsyncIterator[bytes] | None = ...,
        loop: asyncio.AbstractEventLoop | None = ...,
    ) -> None: ...
