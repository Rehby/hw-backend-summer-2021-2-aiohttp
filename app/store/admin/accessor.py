from __future__ import annotations

import typing
from hashlib import sha256

from app.admin.models import Admin
from app.base.base_accessor import BaseAccessor

if typing.TYPE_CHECKING:
    from app.web.app import Application


class AdminAccessor(BaseAccessor):
    async def connect(self, app: Application):
        self.app.database.admins = []
        await self.create_admin(self.app.config.admin.email, self.app.config.admin.password)

    async def create_admin(self, email: str, password: str) -> Admin:
        admin = Admin(
            email=email,
            password=sha256(password.encode("utf-8")).hexdigest(),
            id=self.app.database.next_admin_id,
        )
        self.app.database.admins.append(admin)
        return admin

    async def get_by_email(self, email: str) -> typing.Optional[Admin]:
        for admin in self.app.database.admins:
            if admin.email == email:
                return admin
