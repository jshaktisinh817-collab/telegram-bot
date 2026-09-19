import os
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import Message

# બેઝિક સેટઅપ
logging.basicConfig(level=logging.INFO)

# bot ડેટા અને એડમિન API ઓટો સેટઅપ
API_ID = int(os.environ.get("API_ID", "123456"))  # અહીં api_id નહીં બદલવાની
API_HASH = os.environ.get("API_HASH", "your_api_hash")  # અહીં api_hash નહીં બદલવાની
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")  # અહીં બોટ ટ્રેન અહી નાખવાનું

app = Client("protected_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("👋 હલ્લો! પ્રૉટેક્ટેડ વિડિયો ડાઉનલોડર બૉટ રેડી છે.\n\nકૃપા કરીને મને ટેલિગ્રામની વિડિઓ લિંક મોકલો!")

@app.on_message(filters.text & ~filters.command("start"))
async def download_handler(client, message: Message):
    url = message.text
    if "t.me/" not in url:
        await message.reply_text("❌ કૃપા કરીને સાચી ટેલિગ્રામ લિંક મોકલો!")
        return

    status_msg = await message.reply_text("⏳ વિડિયો પ્રૉસેસ થઈ રહ્યો છે...")

    try:
        # અહીં લિંક ડાઉનલોડ અને અપલોડ કરવાનું લોજિક આવશે
        # (ફક્ત ટેસ્ટ માટે સંદેશ રિપ્લાય કરી દીધો છે)
        await status_msg.edit_text("📥 વિડિયો પ્રૉસેસ થઈ રહ્યો છે, થોડી રાહ જુઓ...")

        # Telegram પર વિડિયો સેવ કરવા માટે Saved Messages માં મોકલવું પણ ચાલુ કરી શકાશે

    except Exception as e:
        await status_msg.edit_text(f"❌ એરર આવી: {str(e)}")

if __name__ == "__main__":
    print("બોટ ચાલુ થઈ રહી છે...")
    app.start()
    idle()
