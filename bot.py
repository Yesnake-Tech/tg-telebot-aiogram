
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


TOKEN = "7955913099:AAHbpJe9-QL46Fxgugq_rUZVGCRhn0WDYi8"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

score = 0
gift = False
channel_url = "t.me/TapClickOfficial"



@dp.message_handler(commands=['start','menu'])
async def start_handler(message: types.Message):
       
        startbutton = KeyboardButton('Кликать!')
        giftbutton = KeyboardButton('Подарок!')
        balancebutton = KeyboardButton('Баланс!')
        channelbutton = KeyboardButton('Наш Канал!')
        Keyboardstart = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(startbutton,giftbutton,balancebutton,channelbutton)
        
        await message.reply(f"@{message.from_user.username} давай начнём?", reply_markup=Keyboardstart)
    
    


@dp.message_handler()
async def start_handler(message: types.Message):
    global score
    global Keyboardmenu
    if message.text == "Кликать!":
        
        score += 1
        menubutton = KeyboardButton('/menu')
        Keyboardmenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menubutton)
        await message.reply(f"+1! Теперь баланс: {score}", reply_markup=Keyboardmenu)
    elif message.text == 'Подарок!':
            global gift
        
            if gift == False:
                menubutton2 = KeyboardButton('/menu')
                Keyboardmenu2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menubutton2)
                gift = True
                await message.reply("спасибо что играите❤️ Баланс +100",reply_markup=Keyboardmenu2)
                score += 100
            
            if gift == True:
                menubutton3 = KeyboardButton('/menu')
                Keyboardmenu3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menubutton3)
                await message.reply("Ты уже забрал(а) подарок😑",reply_markup=Keyboardmenu3)   
    elif    message.text == 'Баланс!':
            menubutton = KeyboardButton('/menu')
            Keyboardmen = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menubutton)
            await message.reply(f"Баланс: {score}", reply_markup=Keyboardmen)

    elif    message.text == 'Наш Канал!':
            global daily
            menubutton = KeyboardButton('/menu')
            Keyboardmen = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menubutton)
            await message.reply(f"Канал {channel_url}", reply_markup=Keyboardmen)
   



if __name__ == "__main__":
    executor.start_polling(dp)