from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button

from lexicon.lexicon import LEXICON_BANK_CARD_HANDLERS
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
    # 4000 0012 3456 7899
    card = text.replace(' ', '')
    if len(card) == 16 and card.isdigit():
        checksum = 0
        cardnumbers = list(map(int, card))
        for count, num in enumerate(cardnumbers):
            if count % 2 == 0:
                buffer = num * 2
                if buffer > 9:
                    buffer -= 9
                checksum += buffer
            else:
                checksum += num
        if checksum % 10 == 0:
            return card
        else:
            raise ValueError
    # print("Неверно набран номер!")
    raise ValueError


async def correct_card_number_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    await message.answer(
        text=LEXICON_BANK_CARD_HANDLERS["correct_card_number_message"].format(
            text
        )
    )


async def error_card_number_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    error: ValueError,
):
    await message.answer(
        text=LEXICON_BANK_CARD_HANDLERS["error_card_number_message"]
    )


async def go_start(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


async def no_text(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    await message.answer(text=LEXICON_BANK_CARD_HANDLERS["non_text_message"])
