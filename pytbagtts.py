
import telebot
from telebot import TeleBot,types
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
from gtts import gTTS



bot = telebot.TeleBot('5143393598:AAEOcKCNxAl7AvPC13vEsvaCs25DsqjRhYc')

def button():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Group',url='t.me/DevelopersChat'),
    InlineKeyboardButton(text='Channel',url='t.me/DevelopersPage'))
    return markup
    
@bot.message_handler(commands=['start'],chat_types=['private'])
def sendWelcome(message):
    user = message.from_user
    user_id = user.id
    first_name = user.first_name
    link_to_profile = f"<a href='tg://user?id={user_id}'>{first_name}</a>" # when you click to user's name you can access their profile.
    bot.send_message(message.chat.id,f'Hello {link_to_profile} how are you\nthis is text to speech bot.for more explanation click /help',parse_mode='HTML',reply_markup=button())

@bot.message_handler(commands=['help'],chat_types=['private'])
def howto_use(message):
    text = '''
 send me any text i will convert it to speech.
 this bot is build by @developerspage 
 please support us by sharing the bot to your friends or you can buy me a coffee:) '''
    bot.send_message(message.chat.id,text)
    
@bot.message_handler(func=lambda m: True)
def textTo_speech(msg):
      text = msg.text
      to_speech = gTTS(text=text,lang='en')
      to_speech.save('result.mp3')
      with open('result.mp3','rb')as file:
          bot.send_voice(msg.chat.id,voice=file,reply_to_message_id = msg.message_id,reply_markup=button())
          
bot.infinity_polling()
      