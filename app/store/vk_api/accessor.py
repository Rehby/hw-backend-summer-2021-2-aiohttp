from __future__ import annotations

import typing

from aiohttp.client import ClientSession

from app.base.base_accessor import BaseAccessor
from app.store.vk_api.dataclasses import Message
from app.store.vk_api.poller import Poller

if typing.TYPE_CHECKING:
    from app.web.app import Application


class VkApiAccessor(BaseAccessor):
    def __init__(self, app: Application, *args, **kwargs) -> None:
        super().__init__(app, *args, **kwargs)
        self.session: typing.Optional[ClientSession] = None
        self.poller: typing.Optional[Poller] = None
        self.key: typing.Optional[str] = None
        self.server: typing.Optional[str] = None
        self.ts: typing.Optional[int] = None

    async def connect(self, app: Application) -> None:
        self.session = ClientSession()
        await self._get_long_poll_service()
        poll = Poller(store=app.store)
        await poll.start()

    async def disconnect(self, app: Application) -> None:
        if self.session is not None:
            await self.session.close()
        if self.poller is not None:
            await self.poller.stop()

    async def _get_long_poll_service(self) -> None:
        ...

    async def poll(self) -> None:
        ...

    async def send_message(self, message: Message) -> None:
        ...
