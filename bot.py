import telebot
import config
import random

complements = [line.rstrip('\n') for line in open('complements.txt',encoding="utf-8"))]
    
bot = telebot.TeleBot(config.token)
GROUP_ID=-1001156157193
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID)
def og_group(message):
    if ("Добр".lower() in message.text.lower() and "утро".lower() in message.text.lower()):
        bot.send_message(message.chat.id,complements[random.randint(0,len(complements)-1)],reply_to_message_id=message.message_id)



GROUP_ID_1=-1001383125195
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID_1)
def test_group(message):
    bot.send_message(message.chat.id, message.chat.id)
    if ("Добр".lower() in message.text.lower() and "утро".lower() in message.text.lower()):
        bot.send_message(message.chat.id,complements[random.randint(0,len(complements)-1)],reply_to_message_id=message.message_id)


if __name__ == '__main__':
    bot.infinity_polling()
