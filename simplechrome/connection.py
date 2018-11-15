# -*- coding: utf-8 -*-
from asyncio import AbstractEventLoop
from typing import Optional, Union


from cripy import Connection, CDPSession, TargetSession, ConnectionType, SessionType

__all__ = [
    "Connection",
    "CDPSession",
    "SessionType",
    "createForWebSocket",
    "ClientType",
    "connection_from_session",
]

ClientType = Union[ConnectionType, SessionType]


async def createForWebSocket(
    url: str, loop: Optional[AbstractEventLoop] = None
) -> Connection:
    return await Connection(url, loop=loop)


def connection_from_session(connection: ClientType) -> ConnectionType:
    while isinstance(connection, (CDPSession, TargetSession)):
        connection = connection._connection
    return connection
