from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler
import nltk

nltk.download('wordnet')
import msg
from services import *
from nltk.corpus import wordnet


def btns(tip=None):
    bts = []
    if tip == "menu":
        bts = [
            [KeyboardButton("School 255 ✈"), KeyboardButton("Test Yechasizmi😊")],
            [KeyboardButton("Bog'lanish 📲"), KeyboardButton("Fikir bildirsh 💬")],
            [KeyboardButton("Anonymous chat 💬")]
        ]
    elif tip == "ha":
        bts = [
            [KeyboardButton("HA")],
            [KeyboardButton("Orqaga🔙")],
        ]
    elif tip == "baho":
        bts = [
            [KeyboardButton("Juda zo‘r 🌟"), KeyboardButton("Yaxshi 👍")],
            [KeyboardButton("Kamchiliklar bor 📚"), KeyboardButton("Menga yoqmadi 👎")],
            [KeyboardButton("Orqaga🔙")],
        ]
    elif tip == "fan":
        bts = [
            [KeyboardButton("📚 DTM majburiy fanlardan testlar 📚")],
            [KeyboardButton("📚 Ingliz tilidan testlar yechish 📚")],
            [KeyboardButton("📚 Matematikadan testlar 📚")],
            [KeyboardButton("👍 Botni baholang 👍"), KeyboardButton("Orqaga🔙")],
        ]
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def inline_btn(btn_type=None, ctg=None, tip=None, bts=None):
    if btn_type == "call":
        btn = [
            [InlineKeyboardButton("Bog'lanish Uchun", url="https://t.me/NuraliyevnaS")],
        ]
    elif btn_type == "fikir":
        btn = [
            [InlineKeyboardButton("Chatga o'tish", url="https://t.me/chat_school255")]
        ]
    elif btn_type == "anonymous":
        btn = [
            [InlineKeyboardButton("Chatga o'tish", url="https://t.me/school255_chat_bot")]
        ]
    else:
        btn = [
            [InlineKeyboardButton("Saytga tashrif ✈", callback_data="sayt", url=""),
             InlineKeyboardButton("Kanal📱", callback_data="sayt", url="https://t.me/school_255")],
        ]

    return InlineKeyboardMarkup(btn)


try:
    create_table()
except Exception as e:
    pass


def start(update, context):
    user = update.message.from_user
    if get_one(user.id):
        a = update.message.from_user.first_name
        print(a)
    else:
        create_user(user_id=user.id, username=user.username)
    update.message.reply_text("<b>Assalomu Alekum</b> {}  😁 \n \n <b>School 255 </b> botiga tashrif "
                              "uchun rahmat 🤝 \n\n Siz botni kezish davomida ko'proq malumot olasiz.\n\n"
                              " O'zingizga kerakli bo'lgan bo'limni tanlang👇🏻"
                              .format(update.message.from_user.first_name),
                              reply_markup=btns("menu"), parse_mode="HTML")


# Definition bilan ishlash

def define(update, context):
    # Get the word to define from the command arguments
    word = ' '.join(context.args)

    # Look up the word definition
    synsets = wordnet.synsets(word)

    # Format the definition as a string
    definition_str = ''
    if synsets:
        for synset in synsets:
            definition_str += f'{synset.name()}:\n'
            definition_str += f'- {synset.definition()}\n'
    else:
        definition_str = "Siz /define noto'g'ri foydalandingiz ❗️\n\nEslatma: Botga avval /define va kiritmoqchi " \
                         "bo'lgan lug'atni kiritasiz. Bot faqat Ingliz tilini qabul qiladi !\n\nNa'muna: \n/define " \
                         "Hello "

    # Send the definition back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=definition_str)


def main():
    Token = "5720438402:AAEHRvGa6P1Yziw6sOyufJ5fNr8uKasV7WE"
    updater = Updater(Token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler('define', define))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, msg.message_handler))
    # updater.dispatcher.add_handler(CallbackQueryHandler(send_document))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
