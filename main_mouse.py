import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
import responses_mouse  # Asegúrate de tener el archivo responses_mouse.py

API_KEY = 'YOUR_TELEGRAM_API_KEY'

# Configuración del logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.info('Iniciando el Bot sobre Mouses...')

# Comandos del Bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Soy tu bot especializado en mouses. ¿Qué necesitas saber?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Puedes preguntar sobre tipos de mouses, características, precios, y más. Usa los comandos /tipos, /caracteristicas, /precios.')

async def tipos_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hay varios tipos de mouses, como óptico, láser, trackball, y más. ¿Cuál te interesa?')

async def caracteristicas_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Los mouses pueden tener distintas características como DPI ajustable, botones programables, etc. ¿Qué característica te interesa?')

async def precios_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Los precios varían según el modelo y las características. ¿Qué tipo de mouse te interesa?')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) dice: {text}')
    response = responses_mouse.get_response(text)
    await update.message.reply_text(response)

# Manejo de errores
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.error(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    # Configurar el bot
    application = ApplicationBuilder().token(API_KEY).build()

    # Añadir manejadores de comandos
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("tipos", tipos_command))
    application.add_handler(CommandHandler("caracteristicas", caracteristicas_command))
    application.add_handler(CommandHandler("precios", precios_command))

    # Añadir manejador de mensajes
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Ejecutar el bot
    application.run_polling()

