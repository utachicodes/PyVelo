from __future__ import annotations

from abc import ABCMeta, abstractmethod
from base64 import b64encode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import HTTPClient


class Authenticator(metaclass=ABCMeta):
    @abstractmethod
    async def get_authorization(self, client: HTTPClient) -> str:
        pass


class BasicAuth(Authenticator):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        secret = f"{self.username}:{self.password}".encode()
        self._header = "Basic " + b64encode(secret).decode("ascii")

    async def get_authorization(self, client: HTTPClient) -> str:
        return self._header
