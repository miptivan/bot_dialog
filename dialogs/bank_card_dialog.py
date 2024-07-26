from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Back, Row, SwitchTo, Url
from aiogram_dialog.widgets.text import Const

from handlers.bank_card_handlers import *
from states.lexicon import LEXICON_BANK_CARD
from states.states import BankCardDialog


bank_card = Dialog(
    Window(
        Const(text=LEXICON_BANK_CARD["start_question"]),
        Row(
            Button(
                text=Const(LEXICON_BANK_CARD["stop_list"]),
                id="stop_list",
                on_click=stop_list,
            ),
            Button(
                text=Const(LEXICON_BANK_CARD["region_card"]),
                id="region_card",
                on_click=region_card,
            ),
        ),
        Button(
            Const(LEXICON_BANK_CARD["back"]),
            id="button_start",
            on_click=go_start,
        ),
        state=BankCardDialog.start,
    ),
    Window(
        Const(text=LEXICON_BANK_CARD["input_card_prompt"]),
        TextInput(
            id="bank_card_input",
            type_factory=bank_card_number_check,
            on_success=correct_card_number_handler,
            on_error=error_card_number_handler,
        ),
        Back(Const(LEXICON_BANK_CARD["back"]), id="back"),
        MessageInput(func=no_text, content_types=ContentType.ANY),
        state=BankCardDialog.input_card,
    ),
    Window(
        Const(text=LEXICON_BANK_CARD["info_text"]),
        Url(
            text=Const(LEXICON_BANK_CARD["info_url_text"]),
            url=Const(LEXICON_BANK_CARD["info_url"]),
            id="info",
        ),
        SwitchTo(
            Const(LEXICON_BANK_CARD["back"]),
            id="to_start",
            state=BankCardDialog.start,
        ),
        state=BankCardDialog.region_card,
    ),
)
