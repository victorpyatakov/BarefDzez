import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater


from exchangers import get_current_exhange

logger = logging.getLogger(__name__)
load_dotenv()


def get_current_exhange_rate(update: Update, context: CallbackContext):
    current_exhange_rate = get_current_exhange()
    context.bot.send_message(update.message.chat_id, '🇷🇺 -> 🇦🇲')
    context.bot.send_message(update.message.chat_id, str(current_exhange_rate))
    logger.info('get_current_exhange_rate -> ', update.effective_user)


def main() -> None:
    token = os.environ.get('TOKEN')
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("rate", get_current_exhange_rate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
