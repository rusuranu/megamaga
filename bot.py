import telebot
import config

bot = telebot.TeleBot(config.token)
GROUP_ID=-1001156157193
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID)
def og_group(message):
    #bot.send_message(message.chat.id, message.chat.id)
    if ("Доброе утро" in message.text):
        bot.send_message(message.chat.id,"Наши девочки самые красивые!",reply_to_message_id=message.message_id)

GROUP_ID_1=-1001383125195
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID_1)
def test_group(message):
    bot.send_message(message.chat.id, message.chat.id)
    if ("Доброе утро" in message.text):
        bot.send_message(message.chat.id,"Наши девочки самые красивые!",reply_to_message_id=message.message_id)


if __name__ == '__main__':
    bot.infinity_polling()