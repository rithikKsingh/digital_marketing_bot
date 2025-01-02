from telegram import Update
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    MessageHandler, 
    ConversationHandler, 
    ContextTypes, 
    filters
)
import requests
from bs4 import BeautifulSoup

# Define conversation states
INDUSTRY, OBJECTIVE, WEBSITE, SOCIAL_MEDIA, PPC, AUDIENCE, LOCATION = range(7)

user_data = {}

# Start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Let's generate relevant keywords for your business.\nWhat industry is your business in?"
    )
    return INDUSTRY

# Collect industry input
async def industry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data['industry'] = update.message.text
    await update.message.reply_text("What is your business objective? (e.g., lead generation, sales, etc.)")
    return OBJECTIVE

# Collect objective
async def objective(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data['objective'] = update.message.text
    await update.message.reply_text("Do you have a website? If yes, please provide the URL.")
    return WEBSITE

# Collect website input
async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data['website'] = update.message.text
    await update.message.reply_text("Do you have any social media platforms? If yes, provide the URL.")
    return SOCIAL_MEDIA

# Collect social media input
async def social_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data['social_media'] = update.message.text
    await update.message.reply_text("Do you use PPC campaigns? (Yes/No)")
    return PPC

# Collect PPC input
async def ppc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data['ppc'] = update.message.text
    await update.message.reply_text("Who are you trying to reach? (e.g., young adults, professionals, etc.)")
    return AUDIENCE

# Collect audience input
async def audience(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data['audience'] = update.message.text
    await update.message.reply_text("What location would you like to target?")
    return LOCATION

# Collect location input and generate keywords
async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data['location'] = update.message.text
    await update.message.reply_text("Thank you! Generating relevant keywords...")
    await generate_keywords(update, context)
    return ConversationHandler.END

# Generate keywords
async def generate_keywords(update: Update, context: ContextTypes.DEFAULT_TYPE):
    industry = user_data.get('industry')
    objective = user_data.get('objective')
    location = user_data.get('location')

    # Example keyword generation logic
    keywords = [
        f"{industry} services in {location}",
        f"Best {industry} solutions for {objective}",
        f"Affordable {industry} providers near {location}",
    ]

    keyword_list = "\n".join(keywords)
    await update.message.reply_text(f"Here are some suggested keywords for your business:\n\n{keyword_list}")

# Cancel the conversation
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Conversation cancelled. Type /start to restart.")
    return ConversationHandler.END

# Main function
def main():
    # Replace "YOUR_TELEGRAM_BOT_TOKEN" with your bot token
    app = ApplicationBuilder().token("7763997569:AAFWq9Jt0j7japZqE6UKv0AS9yKCdAeS2Lc").build()

    # Conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            INDUSTRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, industry)],
            OBJECTIVE: [MessageHandler(filters.TEXT & ~filters.COMMAND, objective)],
            WEBSITE: [MessageHandler(filters.TEXT & ~filters.COMMAND, website)],
            SOCIAL_MEDIA: [MessageHandler(filters.TEXT & ~filters.COMMAND, social_media)],
            PPC: [MessageHandler(filters.TEXT & ~filters.COMMAND, ppc)],
            AUDIENCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, audience)],
            LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, location)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(conv_handler)

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
