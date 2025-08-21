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
    SESSION = os.environ.get("SESSION", "BQGo5ZIAiEi8ZH15WDuCOLhO_ACWqyv2Ogz7FhNY1oDYjTdfkkAud40Lfqn8EtdiNZSAqjpz60-nSzjuFBZSSmHNkUN5zAvSJM4BeQMWPZVsys1EqilAcWE7LysCko92kwXm9iaEthcDOHRlZe8QMvW33K7ithfXyciFYBJih3bkxxlNQ5SztQumFDjtlKZh9n5D-kBUSiYrhPetem8bUh5g_Qz7pqZYLrwH2ZpQ5sVh1f8lgKb00p3q9yTXoyOeyuqHA0fbycXx1yCa8yG6GLQpQzgO98gpfBy8tbx7xmMSBkPqPPoVlTyt_6DOQuDm1Jw03b76moEAjvraqOTyW3HlGMNTSAAAAABOvLKoAA")  # ⚠️ Required @SnowStringGenBot

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
