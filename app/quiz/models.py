from __future__ import annotations

import typing
from dataclasses import dataclass


@dataclass
class Theme:
    id: typing.Optional[int]
    title: str


@dataclass
class Answer:
    title: str
    is_correct: bool


@dataclass
class Question:
    id: typing.Optional[int]
    theme_id: typing.Optional[int]
    title: str
    answers: typing.List[Answer]
