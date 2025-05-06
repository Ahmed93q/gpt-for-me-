import os
from telegram import Update, InputMediaVideo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ضع التوكن هنا أو استخدم متغير بيئة
BOT_TOKEN = os.getenv("BOT_TOKEN", "ضع_توكن_البوت_هنا")

# رابط الفيديو من تليجرام
VIDEO_URL = "https://t.me/a_moment_before/8014"

WELCOME_MESSAGE = "مرحباً بك! هذا هو فيديو moto الذي طلبته."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "moto":
        await update.message.reply_text(WELCOME_MESSAGE)
        await update.message.reply_video(VIDEO_URL)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
