import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "27846034")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "7976191427:AAFYxlIWAaDPPBeYBwgh3GKT1ysfUP_ceGI")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8312957393:AAH1-aotfhS7y0Qg07K0Qn3AhxgX7cr9A48")  # ⚠️ Required

    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://neetfusionin:neetfusionin@cluster0.c7aecmc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME = os.environ.get("DB_NAME", "AutoAcceptBot")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/0ceb5f176f3cf877a08b5.jpg")
    ADMIN = int(os.environ.get('ADMIN', '1320989352'))  # ⚠️ Required
    DEFAULT_WELCOME_MSG = os.environ.get("WELCOME_MSG", "Hey {user},\nYour Request Approved ✅,\n\nWelcome to **{title}**")
    DEFAULT_LEAVE_MSG = os.environ.get("LEAVE_MSG", "By {user},\nSee You Again 👋\n\nFrom **{title}**")

    # user client config
    SESSION = os.environ.get("SESSION", "BQGo5ZIARN69f9l6Wnb0p7YDh8L-82tEKubsrwBF2-NIbqmD88olS63kBejrRN8VHeWNsWrluuR_eYfdRFiTK7VwjsOsgF5_Y5Xmbz800FAYd6KHOVuhcJ6wFA7Ul7CRd0sqiHaaiVVnoZWsSU_D0kFZ20-31ak382NqbApGl846jzORtovEacgEn3FRytNuZjV6kyzP0WsN5sghBNct2NAiN4Dg8wzXzFWyNdrJ9rnsR8hANh_aIq-l7U41_HXbe7w4tKm0ydRaLPnFmM2_xF8jai0qfUr4mESRjV1vqibxJIuR9fY8wWvpilNrJLNOv6s25sCnE9i9veojjfXI5wzVTgVpOQAAAABOvLKoAA")  # ⚠️ Required @SnowStringGenBot

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
