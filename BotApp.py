from bot.bot import Bot
from bot.handler import MessageHandler

TOKEN = "001.2687836354.0305942298:1010906191" #your token here
CHAT = "689061347@chat.agent"
bot = Bot(token=TOKEN)
print("I'm ready!")


def message_cb(bot, event):
    print(event)
    bot.send_text(chat_id=event.from_chat, text=event.text)



bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()
