# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """
Hello {},
I am a simple youtube thumbnail downloader telegram bot.

- Send a youtube video link or video ID.
- I will send the thumbnail.

Made by @ToxicDeeModderr
<p align="center"><a href="https://t.me/DaisySupport_Official"><img src="https://te.legra.ph/file/4e337e6326ae644f49a37.jpg" width="400"></p>
"""

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/TheBotsWorldChannel')   
        ]]
    )
REGEX = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

Bot = Client(
    "YouTube-Thumbnail-Downloader",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@Bot.on_message(filters.private & filters.text)
async def send_thumbnail(bot, update):
    message = await update.reply_text(
        text="`Analysing...`",
        disable_web_page_preview=True,
        quote=True
    )
    if ("youtube.com" in update.text) and ("/" in update.text) and ("=" in update.text):
        id = update.text.split("=")[-1]
    elif ("youtu.be" in update.text) and ("/" in update.text):
        id = update.text.split("/")[-1]
    else:
        id = update.text
    try:
        thumbnail = "https://img.youtube.com/vi/" + id + "/sddefault.jpg"
        await update.reply_photo(
            photo=thumbnail,
            reply_markup=BUTTONS,
            quote=True
        )
        await message.delete()
    except Exception as error:
        await message.edit_text(
            text=error,
            disable_web_page_preview=True,
            reply_markup=BUTTONS
        )
<b>
Use /play <song name> or use /play as a reply to an audio file or youtube link.

Use /yplay to play all the songs of a youtube playlist.

You can also use <code>/splay song name</code> to play a song from Jio Saavn or <code>/splay -a album name</code> to play all the songs from a jiosaavn album or /cplay <channel username or channel id> to play music from a telegram channel.</b>

**Common Commands**:

**/play**  Reply to an audio file or YouTube link to play it or use /play <song name>.
**/splay** Play music from Jio Saavn, Use /splay <song name> or <code>/splay -a album name</code> to play all the songs from that album.
**/player**  Show current playing song.
**/upload** Uploads current playing song as audio file.
**/help** Show help for commands
**/playlist** Shows the playlist.

**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2.
**/cplay** Play music from a channel's music files.
**/yplay** Play music from a youtube playlist.
**/join**  Join voice chat.
**/leave**  Leave current voice chat
**/shuffle** Shuffle Playlist.
**/vc**  Check which VC is joined.
**/stop**  Stop playing.
**/radio** Start Radio.
**/stopradio** Stops Radio Stream.
**/clearplaylist** Clear the playlist.
**/export** Export current playlist
Bot.run()
