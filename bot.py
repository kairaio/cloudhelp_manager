from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("Halo! Bot kamu sudah jalan 🚀")

app = ApplicationBuilder().token("ISI_TOKEN_KAMU").build()
app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling()
