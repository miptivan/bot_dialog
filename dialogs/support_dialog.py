from typing import Any

from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.input import TextInput, MessageInput, ManagedTextInput
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.text import Const

from handlers.support_card_handlers import go_start
from model.model import insert_user_message
from states.states import Support


def text_check(text: Any) -> str:
    if len(text) > 10:
        return text
    raise ValueError


async def correct_text(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    insert_user_message(message)
    await dialog_manager.switch_to(Support.response_waiting)
    await message.answer(text=f'Мы получили сообщение: "{text}"')


async def error_text(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError):
    await message.answer(
        text='Опишите проблему подробнее'
    )


async def no_text(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    print(type(widget))
    await message.answer(text='Опишите проблему текстом')


support = Dialog(
    Window(
        Const(text="Задайте вопрос текстом и оператор поддержки Вам вскоре ответит."),
        TextInput(
            id='text_input',
            type_factory=text_check,
            on_success=correct_text,
            on_error=error_text,
        ),
        MessageInput(
            func=no_text,
            content_types=ContentType.ANY
        ),
        Row(
            Button(
                Const("Назад"),
                id="button_start",
                on_click=go_start,
            ),
        ),
        state=Support.enter_message
    ),
    Window(
        Const(text="Подождите ответа или вернитесь в главное меню"),
        Button(
            Const("Назад"),
            id="button_start",
            on_click=go_start,
        ),
        state=Support.response_waiting
    )
)
