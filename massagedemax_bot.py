import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8861938100:AAGUgIiH1gTQwzznogijF44woQdty6_kgDI"

ANKETA_URL = "https://docs.google.com/forms/d/e/1FAIpQLSex5eswIQXZkLSaG-Vw8qPLtZx-tUt9xprhFG_xx0zPFFQI4g/viewform"
OTZYVY_URL = "https://t.me/massagedetkambrasil"
MAKSIM_URL = "https://t.me/Lost_In_Brazil"
CERT1_URL = "https://drive.google.com/file/d/1omOEZMN8fbEMXMlVmO6YzY6utk3R9jZF/view"
CERT2_URL = "https://drive.google.com/file/d/130LIXPW7JsRbwjgMz70XTXr0bjhUJq8O/view"
CERT3_URL = "https://drive.google.com/file/d/1FIPJwu9lbrObo71NQsD2ViIA4k7zFJRj/view"
CERT4_URL = "https://drive.google.com/file/d/11xCyXxZ1ryzdw0oF4BBzHu49pLq23MJw/view"
ADMIN_ID = 444701400

logging.basicConfig(level=logging.INFO)


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📅 Даты записи", callback_data="dates"),
         InlineKeyboardButton("💆 Цены", callback_data="prices")],
        [InlineKeyboardButton("⭐ Отзывы", callback_data="reviews"),
         InlineKeyboardButton("👋 Обо мне", callback_data="about")],
        [InlineKeyboardButton("🌱 Полезное", callback_data="useful")],
        [InlineKeyboardButton("✉️ Написать Максиму", url=MAKSIM_URL)],
    ]
    await update.message.reply_text(
        "Привет! Я бот Максима — детского массажиста в Бразилии 🇧🇷\n\n"
        "Выберите, что вас интересует:\n\n"
        "🔒 Нажимая кнопки, вы соглашаетесь на обработку ваших данных для записи на массаж.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# /dates
async def dates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📅 *Ближайшие даты записи*\n\n"
        "📍 Рио-де-Жанейро — запись открыта, я здесь почти всегда, за исключением командировок\n"
        "📍 Флорианополис — 15 июня – 4 июля\n"
        "📍 Сан-Паулу — 1 – 10 сентября\n"
        "📍 Сантос — 11 – 21 сентября\n\n"
        "Если вашего города нет в списке — напишите мне, обсудим 🙌"
    )
    keyboard = [
        [InlineKeyboardButton("📝 Заполнить анкету", url=ANKETA_URL)],
        [InlineKeyboardButton("✉️ Написать сообщение", url=MAKSIM_URL)],
    ]
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# /prices
async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📍 Из какого вы города?"
    keyboard = [
        [InlineKeyboardButton("🏙 Рио-де-Жанейро", callback_data="city_rio")],
        [InlineKeyboardButton("🏙 Флорианополис", callback_data="city_other")],
        [InlineKeyboardButton("🏙 Сан-Паулу", callback_data="city_other")],
        [InlineKeyboardButton("🏙 Сантос", callback_data="city_other")],
    ]
    if update.message:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))


PRICES_DESCRIPTION = (
    "Первый визит носит диагностический, ознакомительный характер:\n"
    "• беседуем с мамой и папой\n"
    "• малыш привыкает ко мне и моему голосу\n"
    "• осматриваю, измеряю малыша, прошу сделать упражнения и проверяю рефлексы "
    "(Бабинского, Кусмауля, Ландау и др.)\n"
    "• отвечаю на все вопросы\n\n"
    "⏳ Визит не ограничен по времени — пока у родителей не кончатся вопросы, "
    "а я не сформирую профиль ребёнка.\n\n"
    "После визита вы принимаете решение о курсе и мы определяемся с количеством сеансов.\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "💳 Цены указаны при оплате *PIX*.\n"
    "Оплата наличными или рублями на карту Т-Банка — скидка *5%*."
)

PRICES_KEYBOARD = [
    [InlineKeyboardButton("🙈 Спасибо, дороговато", callback_data="dorogovat")],
    [InlineKeyboardButton("📝 Заполнить анкету", url=ANKETA_URL)],
]


# /reviews
async def reviews(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⭐ *Отзывы родителей о моей работе*\n\n"
        "Читайте, что говорят мамы и папы после сеансов с Максимом 👇"
    )
    keyboard = [
        [InlineKeyboardButton("👀 Смотреть отзывы", url=OTZYVY_URL)],
    ]
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# /contact
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💬 *Остались вопросы?*\n\n"
        "Если у вас есть вопросы по массажу, развитию ребёнка или записи на консультацию — "
        "напишите мне напрямую. Отвечаю быстро 🙂"
    )
    keyboard = [
        [InlineKeyboardButton("✉️ Написать Максиму", url=MAKSIM_URL)],
        [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/massage_for_kids_brasil")],
    ]
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 *Привет, я Максим*\n\n"
        "Рождён в Казахстане, живу между Рио и Занзибаром. Отец троих детей — младшей уже годик 🥰\n\n"
        "Я знаю и понимаю детей, и они отвечают мне взаимностью.\n\n"
        "🎓 *Образование:*\n"
        "1️⃣ Медицинский колледж — диплом\n"
        "2️⃣ Школа детского оздоровительного массажа — сертификат\n"
        "3️⃣ Instituto de Ensino Fisiomassoterapia, Рио-де-Жанейро — сертификат\n"
        "4️⃣ Escola de Massagem Infantil Praxi Enfermagem — сертификат\n\n"
        "🌱 *Помогу с:*\n"
        "• коликами и газиками\n"
        "• проверкой врождённых физиологических рефлексов\n\n"
        "Спокойными движениями и простыми словами — с теплом рук и любовью к каждому маленькому человеку 🤲\n\n"
        "Есть вопросы? Просто напиши 👇"
    )
    keyboard = [
        [InlineKeyboardButton("🎓 Мед. колледж 🇷🇺", url=CERT1_URL),
         InlineKeyboardButton("👶 Детский массаж 🇷🇺", url=CERT2_URL)],
        [InlineKeyboardButton("🌿 Fisiomassoterapia 🇧🇷", url=CERT3_URL),
         InlineKeyboardButton("🤲 Praxi Enfermagem 🇧🇷", url=CERT4_URL)],
        [InlineKeyboardButton("📝 Заполнить анкету", url=ANKETA_URL)],
        [InlineKeyboardButton("✉️ Написать Максиму", url=MAKSIM_URL)],
    ]
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# /useful
async def useful(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌱 *Полезное от Максима*\n\n"
        "Массаж — это здорово. Но большую часть времени ваш малыш проводит с вами, а не со мной. "
        "Именно поэтому мне важно, чтобы вы тоже были в теме.\n\n"
        "Все вокруг знают как правильно — бабушки, соседки, подруги. Я тоже знаю. "
        "Только у меня диплом, три сертификата и трое своих детей 🙈\n\n"
        "Разбираю самые живучие советы — нажмите на любой 👇"
    )
    keyboard = [
        [InlineKeyboardButton("🧦 Ножки должны быть в тепле!", callback_data="tip_nogi")],
        [InlineKeyboardButton("👶 Пусть смотрит на мир — так интереснее!", callback_data="tip_perenoski")],
        [InlineKeyboardButton("🕯 Зачем режим — само устаканится", callback_data="tip_ritualy")],
        [InlineKeyboardButton("😬 На животик? Ему же не нравится!", callback_data="tip_zhivot")],
    ]
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# Обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "dates":
        await dates(update, context)
    elif query.data == "prices":
        await prices(update, context)
    elif query.data == "reviews":
        await reviews(update, context)
    elif query.data == "about":
        await about(update, context)
    elif query.data == "useful":
        await useful(update, context)
    elif query.data == "city_rio":
        text = (
            "💆 *Стоимость услуг — Рио-де-Жанейро*\n\n"
            "*Первый визит — 450 реалов*\n\n"
            + PRICES_DESCRIPTION +
            "\n━━━━━━━━━━━━━━━━━━\n"
            "*Сеанс массажа + ЛФК:*\n"
            "• Разовый сеанс — 400 реалов\n"
            "• Курс из 10 сеансов по предоплате — 3400 реалов\n\n"
        )
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(PRICES_KEYBOARD))
    elif query.data == "city_other":
        city = query.message.text if query.message else ""
        text = (
            "💆 *Стоимость услуг*\n\n"
            "*Первый визит — 450 реалов*\n\n"
            + PRICES_DESCRIPTION +
            "\n━━━━━━━━━━━━━━━━━━\n"
            "*Сеанс массажа + ЛФК:*\n"
            "• Разовый сеанс — 350 реалов\n"
            "• Курс из 10 сеансов по предоплате — 3000 реалов\n\n"
        )
        await query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(PRICES_KEYBOARD))
    elif query.data == "tip_nogi":
        await query.message.reply_text(
            "🧦 *Ножки должны быть в тепле!*\n\n"
            "Крошечные туфельки выглядят adorável. Но как массажист скажу прямо: "
            "обувь на маленьком ребёнке — это помеха развитию.\n\n"
            "Стопа состоит из 26 костей. Чтобы они сформировались правильно, ребёнку нужно "
            "чувствовать поверхность под ногами — текстуру, температуру, неровности. "
            "Именно так развивается баланс, координация и правильный свод стопы.\n\n"
            "В Рио нам особенно повезло — тёплый климат круглый год. Никаких отговорок про "
            "холодный пол 😄 Дома, на пляже, на траве — максимум времени босиком. "
            "Это лучшее, что вы можете сделать для ног вашего малыша прямо сейчас.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📖 Читать источник", url="https://medaboutme.ru/articles/5_prichin_pochemu_detyam_nado_khodit_bosikom/")],
                [InlineKeyboardButton("↩️ К списку советов", callback_data="useful"),
                 InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")],
            ])
        )
    elif query.data == "tip_perenoski":
        await query.message.reply_text(
            "👶 *Пусть смотрит на мир — так интереснее!*\n\n"
            "Слинг и эрго-рюкзак — прекрасные вещи, если подобраны правильно.\n\n"
            "Главное правило — *М-позиция*: колени малыша выше попы, ножки разведены как лягушка. "
            "Это физиологичное положение, которое поддерживает тазобедренные суставы и помогает "
            "избежать дисплазии.\n\n"
            "⚠️ Переноска лицом вперёд — одна из самых частых ошибок. Вес распределяется "
            "неправильно, позвоночник перегружается, бёдра висят без опоры. Хотите чтобы малыш "
            "смотрел на мир — поверните лицом к себе и немного вбок. Мир увидит, а спина "
            "скажет спасибо.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📖 Читать источник", url="https://t.me/slingosveta/2673")],
                [InlineKeyboardButton("↩️ К списку советов", callback_data="useful"),
                 InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")],
            ])
        )
    elif query.data == "tip_ritualy":
        await query.message.reply_text(
            "🕯 *Зачем режим — само устаканится*\n\n"
            "Дети живут в непредсказуемом мире. Ритуалы — это якоря, которые дают ощущение "
            "стабильности и контроля.\n\n"
            "Купание в одно время, одна и та же колыбельная, поглаживание перед сном — сигналы "
            "нервной системе: всё хорошо, можно расслабиться.\n\n"
            "И кстати — массаж работает в разы лучше, когда он тоже становится ритуалом. "
            "Регулярность, спокойная обстановка, знакомые движения. Расслабленный ребёнок — "
            "это совсем другой результат 🤲",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📖 Читать источник", url="https://n-e-n.ru/rituals/")],
                [InlineKeyboardButton("↩️ К списку советов", callback_data="useful"),
                 InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")],
            ])
        )
    elif query.data == "tip_zhivot":
        await query.message.reply_text(
            "😬 *На животик? Ему же не нравится!*\n\n"
            "Это первая гимнастика в жизни ребёнка — и одна из самых важных.\n\n"
            "Когда малыш лежит на животе, он тренирует мышцы шеи, плеч и спины. "
            "Учится держать голову, готовится к переворотам и ползанью. "
            "Плюс — в этой позе лучше отходят газы 🙂\n\n"
            "Начинать можно с первых дней жизни — буквально по 10 секунд. "
            "К трём месяцам хорошо развитый малыш лежит на животе около 10 минут.\n\n"
            "⚠️ Если ребёнок сильно запрокидывает голову и выгибается — "
            "выкладывания лучше пока отложить и показаться специалисту.\n\n"
            "Идеально — 5-10 раз в день между кормлениями. "
            "Это совсем немного, но разница в развитии будет заметна.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📖 Читать источник", url="https://www.novokrinitskii.com/blog/vykladyvanie_na_zhivot")],
                [InlineKeyboardButton("↩️ К списку советов", callback_data="useful"),
                 InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")],
            ])
        )
    elif query.data == "main_menu":
        keyboard = [
            [InlineKeyboardButton("📅 Даты записи", callback_data="dates"),
             InlineKeyboardButton("💆 Цены", callback_data="prices")],
            [InlineKeyboardButton("⭐ Отзывы", callback_data="reviews"),
             InlineKeyboardButton("👋 Обо мне", callback_data="about")],
            [InlineKeyboardButton("🌱 Полезное", callback_data="useful")],
            [InlineKeyboardButton("✉️ Написать Максиму", url=MAKSIM_URL)],
        ]
        await query.message.reply_text(
            "Выберите, что вас интересует:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif query.data == "dorogovat":
        user = query.from_user
        name = user.full_name
        username = f"@{user.username}" if user.username else "без юзернейма"
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"💰 Кто-то считает дороговато!\n\n👤 {name} ({username})\nID: {user.id}"
        )
        await query.message.reply_text(
            "Напишите Максиму напрямую — он постарается найти решение 🙂",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✉️ Написать Максиму", url=MAKSIM_URL)]
            ])
        )


# Запуск
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dates", dates))
    app.add_handler(CommandHandler("prices", prices))
    app.add_handler(CommandHandler("reviews", reviews))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("useful", useful))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен ✅")
    app.run_polling()
