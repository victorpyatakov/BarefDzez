import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters


from exchangers import get_current_exhange, get_amd_rub

import logging

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
load_dotenv()


def get_current_exhange_rate(update: Update, context: CallbackContext):
    current_exhange_rate = get_current_exhange()
    context.bot.send_message(update.message.chat_id, '🇷🇺 -> 🇦🇲')
    context.bot.send_message(update.message.chat_id, str(current_exhange_rate))
    logger.info('get_current_exhange_rate -> ', update.effective_user)


def get_count_rub(update: Update, context: CallbackContext):
    arg = " ".join(context.args)
    if arg:
        amd = float(arg.replace(',', '.'))
        amd_rub = get_amd_rub(amd)
        context.bot.send_message(update.message.chat_id, '🇦🇲 -> 🇷🇺')
        context.bot.send_message(update.message.chat_id, str(amd_rub))
        logger.info('get_count_rub -> ', update.effective_user)
    else:
        context.bot.send_message(update.message.chat_id, 'Please input count of AMD after /rub. ex: /rub 1000')


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text.replace(',', '.')

    if text.replace(".", "", 1).isdigit():
        amd = float(text)
        amd_rub = get_amd_rub(amd)
        context.bot.send_message(update.message.chat_id, '🇦🇲 -> 🇷🇺')
        context.bot.send_message(update.message.chat_id, str(amd_rub))
        logger.info('get_count_rub -> ', update.effective_user)


def main() -> None:
    token = os.environ.get('TOKEN')
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("rate", get_current_exhange_rate))
    dispatcher.add_handler(CommandHandler("rub", get_count_rub))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
