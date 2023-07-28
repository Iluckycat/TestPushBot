from bot.bot import Bot
from bot.handler import MessageHandler
from RunTests import start_run
import os
import zipfile
from pathlib import Path
import io

TOKEN = "001.2687836354.0305942298:1010906191" #your token here
CHAT = "689061347@chat.agent"
bot = Bot(token=TOKEN)
print("I'm ready!")


def message_cb(bot, event):
    print(event)
    if event.text == "Запусти прогон":
        start_run()
        #bot.send_text(chat_id=event.from_chat, text="Прогон завершён!\nРезультаты прогона: ")
        file_rep = open("reports/mockserver.html")
        file_style = open("reports/assets/style.css")
        print(file_style)
        bot.send_text(chat_id=event.from_chat, text="Прогон завершён!\nРезультаты прогона: ")
        zipBuffer = io.BytesIO()
        report = zipfile.ZipFile(zipBuffer, mode="w")
        report.writestr("reports/mockserver.html", file_rep.read())
        report.writestr("reports/assets/style.css", file_style.read())
        zipBuffer.seek(0)
        bot.send_file(chat_id=event.from_chat, file=zipBuffer)
        os.remove(".pytest_cache/v/cache/lastfailed")
    else:
        bot.send_text(chat_id=event.from_chat, text="Отправь фразу: 'Запусти прогон'!")




bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()
