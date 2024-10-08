from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from states.states import (
    BankCardDialog,
    FAQDialog,
    StartSG,
    TransportCardDialog, Support,
)


main_menu = Dialog(
    Window(
        Const(text="Главное меню"),
        Start(
            Const("Банковская карта"),
            id="bank_card",
            state=BankCardDialog.start,
        ),
        Start(
            Const("Транспортная карта"),
            id="transport_card",
            state=TransportCardDialog.start,
        ),
        Start(
            Const("Частые вопросы"), id="faq", state=FAQDialog.window_1
        ),
        Start(
            Const("Поддержка"), id="support", state=Support.enter_message
        ),
        state=StartSG.start,
    )
)
