from bot.bot import Bot
from bot.handler import MessageHandler

TOKEN = "001.2687836354.0305942298:101090619" #your token here

bot = Bot(token=TOKEN)

def message_cb(bot, event):
    bot.send_text(chat_id=event.from_chat, text=event.text)

bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()