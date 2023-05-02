import school


def message_handler(update, context):
    user = update.message.from_user
    msg = update.message.text

    if msg == "School 255 ✈":
        update.message.reply_text("📲 Saytga tashrif buyursangiz ko'proq malumotlarga ega bo'lasiz va bizning. \n \n "
                                  "Kanalga ham ❗ Obuna bo'lib qo'ysangiz Hursand bo'lamiz.",
                                  reply_markup=school.inline_btn("btn"), parse_mode="HTML")

    # AI chat button
    elif msg == "Anonymous chat 💬":
        update.message.reply_photo(photo=open("anonymous.jpg", "rb"),
                                   caption="👋🏻 Salom do'stim ! Siz bu botda tarmoqda online inson "
                                           "bilan\nsuhbatlashishingiz va mini o'ynlar o'ynashingiz mumkin.",
                                   reply_markup=school.inline_btn("anonymous"))

    # English Definitions
    elif msg == "English Definitions 👩🏻‍🏫":
        update.message.reply_photo(photo=open("Test.png", "rb"),
                                   caption="👋🏻 Salom do'stim ! Siz o'zingizga kerakli fandan test yechishga "
                                           "tayyormisiz🤔\n\n Unda test yechishni boshlang ... \n\n O'zingizga kerakli "
                                           "bo'limni tanlang...👇🏻",
                                   reply_markup=school.btns("menu"))

    # bog'lanish
    elif msg == "Bog'lanish 📲":
        update.message.reply_text("Maktab <b>administratsiasi</b> bilan bog'lanish uchun \n<b>(Faqat muhim muammolar "
                                  "uchun !)</b> \n\n "
                                  "❗️Malum Sabablarga ko'ra aloqa yozib olinishi mumkin...",
                                  reply_markup=school.inline_btn("call"), parse_mode="HTML")

    elif msg == "Test Yechasizmi😊":
        update.message.reply_text("Testda o'z bilimingizni tekshirishingiz mumkin agar tayyor bo'lsangiz <b>(HA)</b> "
                                  "tugmasini bosing😃",
                                  reply_markup=school.btns("ha"), parse_mode="HTML")

    # orqaga Back bilan ishlanga qisim
    elif msg == "Orqaga🔙":
        update.message.reply_text("Tashrif uchun rahmat 😃", reply_markup=school.btns("menu"))

    elif msg == "HA":
        update.message.reply_photo(photo=open("Test.png", "rb"),
                                   caption="👋🏻 Salom do'stim ! Siz o'zingizga kerakli fandan test yechishga "
                                           "tayyormisiz🤔\n\n Unda test yechishni boshlang ... \n\n O'zingizga kerakli "
                                           "bo'limni tanlang...👇🏻",
                                   reply_markup=school.btns("fan"))

    # Fikir bildirish buttoni
    elif msg == "Fikir bildirsh 💬":
        update.message.reply_photo(photo=open("chatuchun.png", "rb"),
                                   caption="Siz o'z fikirlaringizni bildirmoqchimisiz unda \nshu yerda yozib "
                                           "qoldiring 👇🏻👇🏻",
                                   reply_markup=school.inline_btn("fikir"))

    # botni baholash qismi
    elif msg == "Juda zo‘r 🌟":
        update.message.reply_text("Rahmat ☺", "Yoqqanidan hursand man")

    elif msg == "Yaxshi 👍":
        update.message.reply_text("Rahmat 👍")

    elif msg == "Kamchiliklar bor 📚":
        update.message.reply_text("Kamchiliklarni ko'rib chiqamiz 😊")

    elif msg == "Menga yoqmadi 👎":
        update.message.reply_text("Iya nega yoqmadi 😕")

    elif msg == "👍 Botni baholang 👍":
        update.message.reply_text("Marhamat botimizni baholang !!!\n\n Rahmat !!!", reply_markup=school.btns("baho"))

    # Test ishlash qismi

    elif msg == "📚 DTM majburiy fanlardan testlar 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open("dtmtest.pdf", "rb"), filename='dtmtest.pdf',
                                  caption="TEST. Asosiy va Majburiy fanlar \nOna tili va Adabiyot \nTarix\nIngliz "
                                          "tili\nRus tili\nMatematika\nFizika\nBiologiya\nKimyo\nGeografiya\n"
                                          "\nO'zizga kerakli fanlardan testlarni yeching.")

    elif msg == "📚 Ingliz tilidan testlar yechish 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open("English_1pdf.pdf", "rb"), filename='English_1pdf.pdf',
                                  caption="English_1.test"),
        context.bot.send_document(chat_id=chat_id, document=open("English_2pdf.pdf", "rb"), filename='English_2pdf.pdf',
                                  caption="English_2.test"),
        context.bot.send_document(chat_id=chat_id, document=open("English_3pdf.pdf", "rb"), filename='English_3pdf.pdf',
                                  caption="English_3.test, Yana test qo'shishimizni hohlasangiz bo'tni baholang 😊")

    elif msg == "📚 Matematikadan testlar 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('matematika.pdf', 'rb'), filename='matematika.pdf',
                                  caption="Matematika fanidan  testlar 📚")

    if msg == "📚 DTM majburiy fanlardan testlar 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('../../../school_152/dtmtest.pdf', 'rb'),
                                  filename='../../../school_152/dtmtest.pdf',
                                  caption="DTM majburiy fandan testlar 📚 agar sizga maqul bo'lgan bo'lsa Botni "
                                          "baholang va biz siz uchun yangi testlar chiqarishga harakat qilamiz.😊")
