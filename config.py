import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "20484052"))
API_HASH = getenv("API_HASH", "9dda8d55ad8c30aa44530abd45786de8")

BOT_TOKEN = getenv("BOT_TOKEN", "5884462911:AAGh1T0odQj5NU5qL9CZ9Wrn96phkHv9ad8")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Bhojpuriya:bhojpuriya@cluster0.osrvhzy.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1001836364647"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", " โคออโข๐๐๐๐๐๐๐ ๊ญ ๐๐๐๐๐ แฏค")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6229909124").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://te.legra.ph/file/3f6a4f4797027a9a8b2b2.mp4")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SpotifyXNetwork")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/BestFriendChattingGroup")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQBc--TXESHfAxB8NGREclG6FwDxuQf_ceYHLs3Cor3GAl4FqGzITWytk9F75Xujgp-v2R1ZrPK1e9d2z7jEdDCRrvL_DRKBvhV4X1Ge8NMmoFdHuvYmRolTVKDyUubsL7mkqHKoXs5VZWT_gf-5TW7h9mekZksrlB37Qb8VjZ9Pt-upljvX2GSZJVnYO7amndt1ZJAIc3MuSAhua8dBJ5tzyc2x9EIqrZ6qDobIeB3D699Cdf9hHT7YtrdGWBhOLCQ5fN1baJ1IRGz-pYHHPTbWVPIJGEyZauVhN5idvecsXWrz3dmTRDGkNzSqW3A9AnREtHBX-qDcYmvWojBqJul-AAAAAXUsU3AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/c24853a89509a99ed5c66.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/31f4492bf586d22411514.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/de6caf94cc5fecdcaa4e9.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/de6caf94cc5fecdcaa4e9.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/c24853a89509a99ed5c66.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/afe4a4fbfce71550898b4.jpg"
