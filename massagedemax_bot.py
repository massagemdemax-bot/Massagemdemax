import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ✅ ВСТАВЬТЕ ВАШ ТОКЕН СЮДА
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
    text = (
        "💆 *Стоимость услуг*\n\n"
        "*Первый визит — 500 реалов*\n\n"
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
        "*Сеанс массажа + ЛФК:*\n"
        "• Разовый сеанс — 450 реалов\n"
        "• Сеанс в рамках курса — 350 реалов\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "💳 Цены указаны при оплате *PIX*.\n"
        "Оплата наличными или рублями на карту Т-Банка — скидка *5%*."
    )
    keyboard = [
        [InlineKeyboardButton("😳 Что-то дороговато", callback_data="dorogovat")],
        [InlineKeyboardButton("📝 Заполнить анкету", url=ANKETA_URL)],
    ]
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


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


# Обработка нажатий на кнопки главного меню
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
    elif query.data == "dorogovat":
        user = query.from_user
        name = user.full_name
        username = f"@{user.username}" if user.username else "без юзернейма"
        # Уведомление Максиму
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"💰 Кто-то считает дороговато!\n\n👤 {name} ({username})\nID: {user.id}"
        )
        # Ответ пользователю
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
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен ✅")
    app.run_polling()
