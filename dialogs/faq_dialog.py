from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Back, Row, SwitchTo, Url
from aiogram_dialog.widgets.text import Const

from handlers.bank_card_handlers import *
from states.lexicon import LEXICON_FAQ_DIALOG
from states.states import BankCardDialog, FAQDialog


faq_dialog = Dialog(
    Window(
        Const(text=LEXICON_FAQ_DIALOG["faq_list"]),
        Button(
            text=Const(LEXICON_FAQ_DIALOG["question_1"]),
            id="question_1",
            on_click=go_start,
        ),
        Button(
            text=Const(LEXICON_FAQ_DIALOG["question_2"]),
            id="question_2",
            on_click=go_start,
        ),
        Button(
            text=Const(LEXICON_FAQ_DIALOG["question_3"]),
            id="question_3",
            on_click=go_start,
        ),
        Button(
            Const(LEXICON_FAQ_DIALOG["back"]),
            id="button_start",
            on_click=go_start,
        ),
        state=FAQDialog.window_1,
    )
)
