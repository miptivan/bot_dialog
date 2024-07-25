from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Back, Button, Row, SwitchTo, Url
from aiogram_dialog.widgets.text import Const

from handlers.bank_card_handlers import (
    bank_card_number_check,
    correct_card_number_handler,
    error_card_number_handler,
    no_text,
)
from handlers.handlers import get_category
from states.states import TransportCardDialog


transport_card = Dialog(
    Window(
        Const(text="У Вас есть транспортная карта?"),
        Row(
            SwitchTo(
                Const("Да"),
                id="have_transport_card",
                state=TransportCardDialog.have_transport_card,
            ),
            SwitchTo(
                Const("Нет"),
                id="no_transport_card",
                state=TransportCardDialog.no_transport_card,
            ),
        ),
        state=TransportCardDialog.start,
    ),
    Window(
        Const(text="Получить транспортную карту можно несколькими способами:"),
        SwitchTo(
            Const("Скачать приложение"),
            id="download_app",
            state=TransportCardDialog.download_app,
        ),
        SwitchTo(
            Const("Получить корпоративную карту"),
            id="get_corporate_card",
            state=TransportCardDialog.get_corporate_card,
        ),
        SwitchTo(
            Const("Получить другую карту"),
            id="get_another_card",
            state=TransportCardDialog.get_another_card,
        ),
        SwitchTo(
            Const("Получить ОТК"),
            id="get_otk",
            state=TransportCardDialog.get_otk,
        ),
        Back(Const("Назад"), id="back"),
        state=TransportCardDialog.no_transport_card,
    ),
    Window(
        Const(text="Скачать приложение\nИнструкция"),
        Url(
            text=Const("Справочная информация"),
            url=Const("https://www.google.ru"),
            id="info",
        ),
        SwitchTo(
            Const("Назад"),
            id="to_start",
            state=TransportCardDialog.no_transport_card,
        ),
        state=TransportCardDialog.download_app,
    ),
    Window(
        Const(text="Получить корпоративную карту\nИнструкция"),
        Url(
            text=Const("Справочная информация"),
            url=Const("https://www.google.ru"),
            id="info",
        ),
        SwitchTo(
            Const("Назад"),
            id="to_start",
            state=TransportCardDialog.no_transport_card,
        ),
        state=TransportCardDialog.get_corporate_card,
    ),
    Window(
        Const(text="Получить другую карту\nИнструкция"),
        Url(
            text=Const("Справочная информация"),
            url=Const("https://www.google.ru"),
            id="info",
        ),
        SwitchTo(
            Const("Назад"),
            id="to_start",
            state=TransportCardDialog.no_transport_card,
        ),
        state=TransportCardDialog.get_another_card,
    ),
    Window(
        Const(text="Получить ОТК\nИнструкция"),
        Url(
            text=Const("Справочная информация"),
            url=Const("https://www.google.ru"),
            id="info",
        ),
        SwitchTo(
            Const("Назад"),
            id="to_start",
            state=TransportCardDialog.no_transport_card,
        ),
        state=TransportCardDialog.get_otk,
    ),
    Window(
        Const(text="Выберите подходящий вариант:"),
        SwitchTo(
            Const("Ввести номер карты"),
            id="input_card_number",
            state=TransportCardDialog.input_card_number,
        ),
        SwitchTo(
            Const("Не знаю номер карты"),
            id="dont_know_card_number",
            state=TransportCardDialog.dont_know_card_number,
        ),
        SwitchTo(
            Const("Назад"),
            id="have_transport_card",
            state=TransportCardDialog.have_transport_card,
        ),
        state=TransportCardDialog.have_transport_card,
    ),
    Window(
        Const(text="Не знаю номер карты\nВыберите подходящую льготу"),
        Button(
            text=Const("Школьник"),
            id="schoolboy",
            on_click=get_category,
        ),
        Button(
            text=Const("Студент"),
            id="student",
            on_click=get_category,
        ),
        Button(
            text=Const("Пенсионер"),
            id="pensioner",
            on_click=get_category,
        ),
        Button(
            text=Const("Льготник"),
            id="beneficiary",
            on_click=get_category,
        ),
        Back(Const("Назад"), id="back"),
        state=TransportCardDialog.dont_know_card_number,
    ),
    Window(
        Const(text="Введите номер карты:"),
        TextInput(
            id="card_input",
            type_factory=bank_card_number_check,
            on_success=correct_card_number_handler,
            on_error=error_card_number_handler,
        ),
        SwitchTo(
            Const("Назад"),
            id="have_transport_card",
            state=TransportCardDialog.have_transport_card,
        ),
        MessageInput(func=no_text, content_types=ContentType.ANY),
        state=TransportCardDialog.input_card_number,
    ),
)
