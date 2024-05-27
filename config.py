from enum import Enum

# BOT_TOKEN = getenv('7040330482:AAFKB2ErTOXxSjsjMu-FrAU__SEWalve6aY)'
BOT_TOKEN = '7040330482:AAFKB2ErTOXxSjsjMu-FrAU__SEWalve6aY'
CHANNEL_ID = 'pksdfnqweopfwe'
GROUP_ID = 'sfoijfjenfonwe'
LOGO_URL = 'http://127.0.0.1:8000/static/app/images/logo2.png'
LOGO_FILE_ID = 'AgACAgIAAxkDAAPUZlCoRe5kqVwPnmLyK8FUi5XuN_gAAvziMRsIVYhKjeMVf5w4DfoBAAMCAANtAAM1BA'


class TelegramEmoji(Enum):
    STAR = '⭐️'
    CART = '🛒'
    SHOP = '🛍'
    PERSON = '👤'
    CHECK = '✅'
    X = '❌'
    BACK = '🔙'

    def __str__(self):
        return self.value
