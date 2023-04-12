#--------------------------------------------
from aiogram import Bot,types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bs4 import BeautifulSoup
import requests
#--------------------------------------------

TOK = "you token"

bot = Bot(token=TOK)
dp = Dispatcher(bot)





@dp.message_handler(commands=['start'])
async def start(message : types.Message):
    await message.reply("Hello this is weather bot")
    await message.answer("to find out the weather in your city, write /weather your city")





@dp.message_handler(commands=['weather'])
async def comand(message : types.Message):
    try:
        namecity = (message.text.split()[1])
        URL = "https://sinoptik.ua/погода-" + namecity
        print(URL)

        r = requests.get(URL)
        
        
        
        soup = BeautifulSoup(r.content, 'html.parser')
        
        
        for el in soup.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
            text = el.select('.wDescription .description')[0].text
           
           
        await message.reply(text="в "+ namecity +" сегодня: " + t_min + ',' + t_max + ',' + text)

    except:
        await message.reply("нету такого города " + namecity)



executor.start_polling(dp, skip_updates=True)