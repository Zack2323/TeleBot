import os
import telebot


hellos= ["hello","hi","hey"]
goodbyes = ["See ya","Take Care!","Bye","bye"]
schoolDays = ["monday","wednesday","friday"]
my_secret = os.environ['API_KEY']


bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands="start")
def greet(message):
  bot.send_message(message.chat.id, "Hello, How can I help you today? Please select or type /help at any time to see what else I can do")

@bot.message_handler(commands="help")
def help(message):
  bot.send_message(message.chat.id, "For your schedules please type in the day, i.e, for Monday's Schedule type /monday")

  """please select or type the day"""

@bot.message_handler(commands=hellos)
def hello(message):
  bot.send_message(message.chat.id, "Hey! Hows it going?")

@bot.message_handler(commands=goodbyes)
def goodbye(message):
  bot.send_message(message.chat.id, "Have a great day!")

@bot.message_handler(commands = schoolDays)
def schedule(message):
  bot.send_message(message.chat.id, "Monday's Schedule You have your CS3201 class at 2pm and CS3602 class at 4pm")



bot.polling()