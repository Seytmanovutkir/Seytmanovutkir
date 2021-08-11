from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from my_token import token

isFriendly = True
moods = ["happy","sad","ok", "bored"]

def start_message(update:Update, context: CallbackContext):
    reply_markup = ReplyKetboardMarkup(
        [
            [KeyboardButton('Hi'),KeyboardButton('How are you?')]
        ]
    )
    context.bot.send_message(update.message.chat.id, """Salom men test bot man. Siz Hi yoki How are you? deb yozishingiz mumkin.""",
                             reply_markup = reply_markup)
def hi_message(update:Update):
    if(not isFriendly): return
    update.message.reply_text("Salom, Men sizni ko'rganimdan xursandman")
def how_message(update:Update):
    mood = choice(moods)
    update.message.reply_text("Men {}".format(mood))
def selector(update:Update, context: CallbackContext):
    text = update.message.text
    if (text == 'Hi'):
        hi_message(update)
    elif (text == 'How are you?'):
        how_message(update)


updater = Updater(token)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler(['start', 'help'],start_message))
dispatcher.add_handler(MessageHandler(Filters.text, selector))
updater.start_polling()

updater.idle()
