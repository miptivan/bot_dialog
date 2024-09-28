from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    start = State()


class BankCardDialog(StatesGroup):
    start = State()
    input_card = State()
    region_card = State()


class TransportCardDialog(StatesGroup):
    start = State()
    no_transport_card = State()
    have_transport_card = State()
    download_app = State()
    get_corporate_card = State()
    get_another_card = State()
    get_otk = State()
    input_card_number = State()
    dont_know_card_number = State()


class FAQDialog(StatesGroup):
    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()


class Support(StatesGroup):
    enter_message = State()
    response_waiting = State()
    window_3 = State()
    window_4 = State()
