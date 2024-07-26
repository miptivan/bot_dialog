from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Back, Button, Row, SwitchTo, Url
from aiogram_dialog.widgets.text import Const

from handlers.bank_card_handlers import (  # Потом будут написаны хендлеры конкретно для transport_card
    bank_card_number_check,
    correct_card_number_handler,
    error_card_number_handler,
    no_text,
)
from handlers.transport_card_handlers import get_category, go_start
from lexicon.lexicon import LEXICON_TRANSPORT_CARD
from states.states import TransportCardDialog


transport_card = Dialog(
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["start_question"]),
        Row(
            SwitchTo(
                Const(LEXICON_TRANSPORT_CARD["yes"]),
                id="have_transport_card",
                state=TransportCardDialog.have_transport_card,
            ),
            SwitchTo(
                Const(LEXICON_TRANSPORT_CARD["no"]),
                id="no_transport_card",
                state=TransportCardDialog.no_transport_card,
            ),
        ),
        Button(
            Const(LEXICON_TRANSPORT_CARD["back"]),
            id="button_start",
            on_click=go_start,
        ),
        state=TransportCardDialog.start,
    ),
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["get_transport_card_options"]),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["download_app"]),
            id="download_app",
            state=TransportCardDialog.download_app,
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["get_corporate_card"]),
            id="get_corporate_card",
            state=TransportCardDialog.get_corporate_card,
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["get_another_card"]),
            id="get_another_card",
            state=TransportCardDialog.get_another_card,
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["get_otk"]),
            id="get_otk",
            state=TransportCardDialog.get_otk,
        ),
        Back(Const(LEXICON_TRANSPORT_CARD["back"]), id="back"),
        state=TransportCardDialog.no_transport_card,
    ),
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["download_app"]),
        Const(text=LEXICON_TRANSPORT_CARD["download_app_instruction"]),
        Url(
            text=Const(LEXICON_TRANSPORT_CARD["info_url_text"]),
            url=Const(LEXICON_TRANSPORT_CARD["download_app_info_url"]),
            id="info",
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["back"]),
            id="to_start",
            state=TransportCardDialog.no_transport_card,
        ),
        state=TransportCardDialog.download_app,
    ),
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["get_corporate_card"]),
        Const(text=LEXICON_TRANSPORT_CARD["get_corporate_card_instruction"]),
        Url(
            text=Const(LEXICON_TRANSPORT_CARD["info_url_text"]),
            url=Const(LEXICON_TRANSPORT_CARD["get_corporate_card_info_url"]),
            id="info",
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["back"]),
            id="to_start",
            state=TransportCardDialog.no_transport_card,
        ),
        state=TransportCardDialog.get_corporate_card,
    ),
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["get_another_card"]),
        Const(text=LEXICON_TRANSPORT_CARD["get_another_card_instruction"]),
        Url(
            text=Const(LEXICON_TRANSPORT_CARD["info_url_text"]),
            url=Const(LEXICON_TRANSPORT_CARD["get_another_card_info_url"]),
            id="info",
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["back"]),
            id="to_start",
            state=TransportCardDialog.no_transport_card,
        ),
        state=TransportCardDialog.get_another_card,
    ),
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["get_otk"]),
        Const(text=LEXICON_TRANSPORT_CARD["get_otk_instruction"]),
        Url(
            text=Const(LEXICON_TRANSPORT_CARD["info_url_text"]),
            url=Const(LEXICON_TRANSPORT_CARD["get_otk_info_url"]),
            id="info",
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["back"]),
            id="to_start",
            state=TransportCardDialog.no_transport_card,
        ),
        state=TransportCardDialog.get_otk,
    ),
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["choose_option"]),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["input_card_number"]),
            id="input_card_number",
            state=TransportCardDialog.input_card_number,
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["dont_know_card_number"]),
            id="dont_know_card_number",
            state=TransportCardDialog.dont_know_card_number,
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["back"]),
            id="have_transport_card",
            state=TransportCardDialog.start,
        ),
        state=TransportCardDialog.have_transport_card,
    ),
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["unknown_card_number_prompt"]),
        Button(
            text=Const(LEXICON_TRANSPORT_CARD["schoolboy"]),
            id="schoolboy",
            on_click=get_category,
        ),
        Button(
            text=Const(LEXICON_TRANSPORT_CARD["student"]),
            id="student",
            on_click=get_category,
        ),
        Button(
            text=Const(LEXICON_TRANSPORT_CARD["pensioner"]),
            id="pensioner",
            on_click=get_category,
        ),
        Button(
            text=Const(LEXICON_TRANSPORT_CARD["beneficiary"]),
            id="beneficiary",
            on_click=get_category,
        ),
        Back(Const(LEXICON_TRANSPORT_CARD["back"]), id="back"),
        state=TransportCardDialog.dont_know_card_number,
    ),
    Window(
        Const(text=LEXICON_TRANSPORT_CARD["enter_card_number"]),
        TextInput(
            id="card_input",
            type_factory=bank_card_number_check,
            on_success=correct_card_number_handler,
            on_error=error_card_number_handler,
        ),
        SwitchTo(
            Const(LEXICON_TRANSPORT_CARD["back"]),
            id="have_transport_card",
            state=TransportCardDialog.have_transport_card,
        ),
        MessageInput(func=no_text, content_types=ContentType.ANY),
        state=TransportCardDialog.input_card_number,
    ),
)
