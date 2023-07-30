from datetime import datetime as dt
import time
from bot.bot import Bot
from bot.handler import MessageHandler
import RunTests
import BotFunc
import schedule
import importlib
import sys

TOKEN = "001.2687836354.0305942298:1010906191" #Your token here
CHAT_ID = "689061347@chat.agent" #Chat id for monitoring tasks
bot = Bot(token=TOKEN)
print("I'm ready!")


def message_cb(bot, event):
    print(event)
    print(event.from_chat)
    if event.text == "Запусти прогон":
        RunTests.start_run()
        bot.send_text(chat_id=event.from_chat, text="Прогон завершён!\nРезультаты прогона: ")
        zipBuffer = BotFunc.MakeZip()
        zipBuffer.seek(0)
        bot.send_file(chat_id=event.from_chat, file=zipBuffer)
    else:
        bot.send_text(chat_id=event.from_chat, text="Отправь фразу: 'Запусти прогон'!")


def scheduled_start():
    print(str(dt.now()) + " старт мониторинга\n")
    RunTests.start_run()
    failed, summary, tests_list = BotFunc.ParseReport()
    if failed == 0:
        bot.send_text(chat_id=CHAT_ID, text=str(dt.now()) + " мониторинг завершён\nРезультаты: \n" + BotFunc.MakeReport(summary))
    else:
        bot.send_text(chat_id=CHAT_ID, text=BotFunc.MakeFailedReport(tests_list))


schedule.every(30).minutes.do(scheduled_start)

bot.dispatcher.add_handler(MessageHandler(callback=message_cb))

bot.start_polling()
bot.idle()

