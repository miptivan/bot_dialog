from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Row, Back, Url, SwitchTo
from aiogram_dialog.widgets.text import Const

from handlers.bank_card_handlers import *
from states.states import BankCardDialog

bank_card = Dialog(
    Window(
        Const(text='Какая у вас проблема с банковской картой?'),
        Row(
        Button(
            text=Const('Стоп-лист'),
            id='stop_list',
            on_click=stop_list),
        Button(
            text=Const('Карта регионов'),
            id='region_card',
            on_click=region_card),
        ),
        Button(Const('Назад'), id='button_start', on_click=go_start),
        state=BankCardDialog.start
    ),
    Window(
        Const(text='Введите номер карты, чтобы создать обращение'),
        TextInput(
            id='bank_card_input',
            type_factory=bank_card_number_check,
            on_success=correct_card_number_handler,
            on_error=error_card_number_handler,
        ),
        Back(Const('Назад'), id='back'),
        MessageInput(
            func=no_text,
            content_types=ContentType.ANY
        ),
        state=BankCardDialog.input_card
    ),
    Window(
        Const(text='Вывод справочной информации по карте регионов'),
        Url(text=Const('Справочная информация'),
            url=Const('https://www.google.ru/'),
            id='info'),
        SwitchTo(Const('Назад'), id='to_start', state=BankCardDialog.start),
        state=BankCardDialog.region_card
    )
)