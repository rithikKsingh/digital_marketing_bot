from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()
# Bot Token
Token = os.getenv("TELEGRAM_BOT_TOKEN")

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to project 001")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This particular message
        /content -> About various playlist of random channel
        /Python -> The first video from python playlist
        /SQL -> The first video from SQL playlist
        /Java -> The first video from Java playlist
        /contact -> contact information
        """
    )

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("We have various playlist and articles available")

async def python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tut link: https://youtu.be/Q59X518JZHE?si=xehURYsRPXdACjhT")

async def sql(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tut link: https://youtu.be/pFq1pgli0OQ?si=DsE458K2te085HEu")

async def java(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tut link: https://youtu.be/i6AZdFxTK9I?si=xye_AOKoLnaK7Qja")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Email: temp@temp.com")

# Create the Application
application = Application.builder().token(Token).build()

# Add command handlers to the dispatcher
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help_command))
application.add_handler(CommandHandler('content', content))
application.add_handler(CommandHandler('Python', python))
application.add_handler(CommandHandler('SQL', sql))
application.add_handler(CommandHandler('Java', java))
application.add_handler(CommandHandler('contact', contact))

# Start the bot
if __name__ == '__main__':
    application.run_polling()