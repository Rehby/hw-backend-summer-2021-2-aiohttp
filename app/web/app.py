from __future__ import annotations

import typing

from aiohttp.web import Application as AiohttpApplication
from aiohttp.web import Request as AiohttpRequest
from aiohttp.web import View as AiohttpView
from aiohttp_apispec import setup_aiohttp_apispec
from aiohttp_session import setup as setup_aiohttp_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from app.admin.models import Admin
from app.store import Store, setup_store
from app.store.database.database import Database
from app.web.config import Config, setup_config
from app.web.logger import setup_logging
from app.web.middlewares import setup_middlewares
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    config: typing.Optional[Config] = None
    store: typing.Optional[Store] = None
    database: typing.Optional[Database] = None


class Request(AiohttpRequest):
    admin: typing.Optional[Admin] = None

    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

    @property
    def store(self) -> Store:
        return self.request.app.store

    @property
    def data(self) -> dict:
        return self.request.get("data", {})


app = Application()


def setup_app(config_path: str) -> Application:
    setup_config(app, config_path)
    setup_aiohttp_apispec(app)
    setup_logging(app)
    setup_routes(app)
    setup_aiohttp_session(app, EncryptedCookieStorage(app.config.session.key))
    setup_middlewares(app)
    setup_store(app)
    return app
