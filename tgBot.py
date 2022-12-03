import os
import telegram
from dotenv import load_dotenv


load_dotenv()
TG_TOKEN = os.environ['TG_TOKEN']
bot = telegram.Bot(token=TG_TOKEN)
print(bot.get_me())

bot.send_message(chat_id='@number_1_space_bot', text="Hello")


bot.send_document(chat_id='@number_1_space_bot', document=open('images/1epic_1b_20221201015632.png', 'rb'))









