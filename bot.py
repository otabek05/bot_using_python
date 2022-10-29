import db 
import weather


from aiogram import Bot, Dispatcher,executor
from aiogram.types import Message

TOKEN="5670030245:AAHB14ck5ramUTFzGlUIvB0QTzBLsJ5Ju-Y"

bot =Bot(token=TOKEN)

dp=Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start(message:Message):
    chat_id=message.from_user.id
    await bot.send_message(
    chat_id=chat_id,
    text=f"Assalomu alaykum"
)



executor.start_polling(dispatcher=dp)