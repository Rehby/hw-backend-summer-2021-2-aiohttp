import typing

from app.base.base_accessor import BaseAccessor
from app.quiz.models import Answer, Question, Theme


class QuizAccessor(BaseAccessor):
    async def create_theme(self, title: str) -> Theme:
        theme = Theme(id=self.app.database.next_theme_id, title=str(title))
        self.app.database.themes.append(theme)
        return theme

    async def create_question(
        self, title: str, theme_id: int, answers: typing.List[Answer]
    ) -> Question:
        question = Question(
            id=self.app.database.next_question_id,
            title=str(title),
            theme_id=theme_id,
            answers=answers,
        )
        self.app.database.questions.append(question)
        return question

    async def get_theme_by_title(self, title: str) -> typing.Optional[Theme]:
        return await self.get_theme_by("title", title)

    async def get_theme_by_id(self, id: int) -> typing.Optional[Theme]:
        return await self.get_theme_by("id", id)

    async def get_theme_by(self, attribute: str, value: typing.Any) -> typing.Optional[Theme]:
        for theme in self.app.database.themes:
            if getattr(theme, attribute) == value:
                return theme

    async def get_question_by(
        self, attribute: str, value: typing.Any
    ) -> typing.Optional[Question]:
        for question in self.app.database.questions:
            if getattr(question, attribute) == value:
                return question

    async def list_themes(self) -> typing.List[Theme]:
        return self.app.database.themes

    async def list_questions(self) -> typing.List[Question]:
        return self.app.database.questions
