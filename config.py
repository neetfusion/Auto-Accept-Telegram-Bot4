import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "27846034")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "980caee71c20f6babaf86d985f5af9e5")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8312957393:AAH1-aotfhS7y0Qg07K0Qn3AhxgX7cr9A48")  # ⚠️ Required

    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://neetfusionin:neetfusionin@cluster0.c7aecmc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME = os.environ.get("DB_NAME", "AutoAcceptBot")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "file:///C:/Users/mdzak/Downloads/photo_2025-08-21_20-09-44.jpg")
    ADMIN = int(os.environ.get('ADMIN', '1320989352'))  # ⚠️ Required
    DEFAULT_WELCOME_MSG = os.environ.get("WELCOME_MSG", "Hey {user},\nYour Request Approved ✅,\n\nWelcome to **{title}**")
    DEFAULT_LEAVE_MSG = os.environ.get("LEAVE_MSG", "By {user},\nSee You Again 👋\n\nFrom **{title}**")

    # user client config
    SESSION = os.environ.get("SESSION", "BQGo5ZIANwWyEwvrvxQcIL4k1BNc1rl0yk0T0jkAH0hPlMogKFsoxWK2IOyLYn-QaqfUrd8ZSBHorA74zDH1iJ2Y-K5OpB1BI7eDPGXJ4v6GhXaFtmbtCa1R4wmKHlaVjve1xnVHRPZY0ZQy5J36a7sY1oDLDMizchDA8o6Ohxcr1cKGas0xzxan9vt3Z5EGYEBm6bCkqvbMFeEhSg6Lb5RNGThoIyOIVMQYdZ7PM90hsGNLXDeKG9Gg87n18r8ZQ3Cb7BB5xIwSTwXsdyxVfmiK0270b37HBTFyoo9A6V50Rsw7Wq3T5mZF04j0nugNFgue3gtYapojwyGkZMaZk5ZrAqlwAAAABOvLKoAA")  # ⚠️ Required @SnowStringGenBot

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class TxT(object):

    HELP_MSG = """
<b> ADMIN Available commands:- </b>

➜ /set_welcome - To set custom welcome message (support photo & video & animation or gif)
➜ /set_leave - To set custom leave message (support photo & video & animation or gif)
➜ /option - To toggle your welcome & leave message also auto accept (whether it'll show to user or not and will auto accept or not)
➜ /auto_approves - To toggle your auto approve channel or group
➜ /status - To see status about bot
➜ /restart - To restart the bot
➜ /broadcast - To brodcast the users (only those user who has started your bot)
➜ /acceptall - To accept all the pending join requests
➜ /declineall - To decline all the pending join requests

⚠️ <b> Support HTML & Markdown formating in welcome or leave message for more info <a href=https://core.telegram.org/api/entities#:~:text=%2C%20MadelineProto.-,Allowed%20entities,-For%20example%20the> Link </a>. </b>


<b>⦿ Developer:</b> <a href=https://t.me/Snowball_Official>ѕησωвαℓℓ ❄️</a>
"""
