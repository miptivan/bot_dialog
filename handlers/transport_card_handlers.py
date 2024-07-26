from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from states.lexicon import LEXICON_TRANSPORT_CARD_HANDLERS
from states.states import StartSG, TransportCardDialog


async def go_start(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


async def download_tts_app(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.switch_to(state=TransportCardDialog.no_transport_card)


async def get_category(
    callback: CallbackQuery, button: Button, manager: DialogManager
):
    manager.dialog_data["category"] = callback.data
    await callback.answer(
        LEXICON_TRANSPORT_CARD_HANDLERS["greeting_message"].format(
            callback.data
        )
    )
    await manager.done()
