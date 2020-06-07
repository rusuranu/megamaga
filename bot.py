import telebot
import config
import random

complements = [line.rstrip('\n') for line in open('complements.txt',encoding="utf-8")]
greetings = [line.rstrip('\n') for line in open('greetings.txt',encoding="utf-8")]
    
bot = telebot.TeleBot(config.token)
GROUP_ID=-1001156157193
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID)
def og_group(message):
    if ("Добр".lower() in message.text.lower() and "утр".lower() in message.text.lower()):
        bot.send_message(message.chat.id,complements[random.randint(0,len(complements)-1)],reply_to_message_id=message.message_id)
        return 0
    if (("привет".lower() in message.text.lower()) or
        ("добрый день".lower() in message.text.lower()) or
        ("Здравствуйте".lower() in message.text.lower()) or
        ("доброго дня".lower() in message.text.lower()) or
        ("доброго вечера".lower() in message.text.lower()) or
        ("добрый вечер".lower() in message.text.lower()) or
        ("здрасти".lower() in message.text.lower()) and
        not (("приветливый".lower() in message.text.lower())
            )
        ):
        try:
            bot.send_message(message.chat.id,
                         greetings[random.randint(0,len(greetings)-1)].replace('%name%',message.from_user.first_name),
                         reply_to_message_id=message.message_id)
        except Exception:
            bot.send_message(message.chat.id,
                         greetings[random.randint(0,len(greetings)-1)],
                         reply_to_message_id=message.message_id)
        return 0



GROUP_ID_1=-1001383125195
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID_1)
def test_group(message):
    #bot.send_message(message.chat.id, message.chat.id)
    if ("Добр".lower() in message.text.lower() and "утр".lower() in message.text.lower()):
        bot.send_message(message.chat.id,complements[random.randint(0,len(complements)-1)],reply_to_message_id=message.message_id)
        return 0
    if (("привет".lower() in message.text.lower()) or
        ("добрый день".lower() in message.text.lower()) or
        ("Здравствуйте".lower() in message.text.lower()) or
        ("доброго дня".lower() in message.text.lower()) or
        ("доброго вечера".lower() in message.text.lower()) or
        ("добрый вечер".lower() in message.text.lower()) or
        ("здрасти".lower() in message.text.lower()) and
        not (("приветливый".lower() in message.text.lower())
            )
        ):
        bot.send_message(message.chat.id,
                         greetings[random.randint(0,len(greetings)-1)].replace('%name%',message.from_user.username),
                         reply_to_message_id=message.message_id)
        return 0

if __name__ == '__main__':
    bot.infinity_polling()
