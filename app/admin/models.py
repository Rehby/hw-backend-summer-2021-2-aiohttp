from __future__ import annotations

import typing
from dataclasses import dataclass


@dataclass
class Admin:
    id: int
    email: str
    password: typing.Optional[str] = None
