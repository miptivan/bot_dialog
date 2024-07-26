from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button

from states.lexicon import LEXICON_BANK_HANDLERS
from states.states import BankCardDialog, StartSG


async def stop_list(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.next()


async def region_card(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.switch_to(state=BankCardDialog.region_card)


def bank_card_number_check(text: str) -> str:
    # Здесь будет проверка по алгоритму Луна
    if all(ch.isdigit() for ch in text):
        return text
    raise ValueError


async def correct_card_number_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer(
        text=LEXICON_BANK_HANDLERS["correct_card_number_message"].format(text)
    )


async def error_card_number_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    error: ValueError,
):
    await message.answer(
        text=LEXICON_BANK_HANDLERS["error_card_number_message"]
    )


async def go_start(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


async def no_text(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    await message.answer(text=LEXICON_BANK_HANDLERS["non_text_message"])
