from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram_dialog.api.exceptions import UnknownIntent, UnknownState


class UnknownIntentMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        try:
            await handler(event, data)
        except UnknownIntent:
            dialog_manager = data.get("dialog_manager")
            print("UnknownIntent")
            if dialog_manager:
                await dialog_manager.start(self.init_state, mode=self.mode)
            await event.callback_query.answer()


class UnknownStateMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        try:
            await handler(event, data)
        except UnknownState:
            dialog_manager = data.get("dialog_manager")
            print("UnknownState")
            if dialog_manager:
                await dialog_manager.start(self.init_state, mode=self.mode)
            await event.callback_query.answer()
