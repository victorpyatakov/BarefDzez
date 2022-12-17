import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logger = logging.getLogger(__name__)
from exchangers import get_current_exhange


def get_current_exhange_rate(update: Update, context: CallbackContext):
    current_exhange_rate = get_current_exhange()
    context.bot.send_message(update.message.chat_id, f'🇷🇺 -> 🇦🇲' ) 
    context.bot.send_message(update.message.chat_id, str(current_exhange_rate))
    logger.info('get_current_exhange_rate -> ', update.effective_user)
    

def main() -> None:
    updater = Updater("5621388544:AAHskp4GjZria_luLZW83PTKYibsmWRbax4")

    # Get the dispatcher to register handlers
    # Then, we register each handler and the conditions the update must meet to trigger it
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("rate", get_current_exhange_rate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
