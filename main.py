import logging
import os

from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters


from exchangers import get_current_exhange, get_amd_rub

import logging

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
load_dotenv()

AMD = 'AMD'
USD = 'USD'
buttons = [[KeyboardButton(AMD)], [KeyboardButton(USD)]]

CONVERT = 'Конвертировать'
button_convert = [[KeyboardButton(CONVERT)]]


def get_current_exhange_rate(update: Update, context: CallbackContext):
    current_exhange_rate = get_current_exhange()
    context.bot.send_message(update.message.chat_id, '🇷🇺 -> 🇦🇲')
    context.bot.send_message(update.message.chat_id, str(current_exhange_rate))
    logger.info('get_current_exhange_rate -> ', update.effective_user)


def get_count_rub(update: Update, context: CallbackContext):
    arg = " ".join(context.args)
    if arg:
        amd = float(arg)
        amd_rub = get_amd_rub(amd)
        context.bot.send_message(update.message.chat_id, '🇦🇲 -> 🇷🇺')
        context.bot.send_message(update.message.chat_id, str(amd_rub))
        logger.info('get_count_rub -> ', update.effective_user)
    else:
        context.bot.send_message(update.message.chat_id, 'Please input count of AMD after /rub. ex: /rub 1000')


def start_command(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # buttons = [[KeyboardButton(AMD)], [KeyboardButton(USD)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choice currency",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def message_handler(update: Update, context: CallbackContext) -> int:
    if AMD in update.message.text:
        context.bot.send_message(update.effective_chat.id, 'Введите Рубли',
                                 reply_markup=ReplyKeyboardRemove(buttons))



def main() -> None:
    token = os.environ.get('TOKEN')
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("rate", get_current_exhange_rate))
    dispatcher.add_handler(CommandHandler("rub", get_count_rub))
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
