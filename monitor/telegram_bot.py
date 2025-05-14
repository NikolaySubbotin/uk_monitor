import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

from django.conf import settings
from monitor.models import Message as TgMessage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_message(update: Update, context: CallbackContext):
    # Сохраняем каждое входящее сообщение
    TgMessage.objects.create(
        chat_id=str(update.effective_chat.id),
        user_id=str(update.effective_user.id),
        text=update.message.text
    )
    update.message.reply_text("Сообщение получено!")

def main():
    updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()