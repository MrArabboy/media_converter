from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from apps.subscriber.models import Language


def language_buttons():
    buttons = []
    two_buttons = []
    languages = Language.objects.all()

    for language in languages:
        two_buttons.append(
            InlineKeyboardButton(language.name, callback_data=language.name)
        )
        if len(two_buttons) == 3:
            buttons.append(two_buttons)
            two_buttons.clear()
    if languages.count() % 3 != 0:
        buttons.append(two_buttons)
    return InlineKeyboardMarkup(buttons)
