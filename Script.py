import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://atglinks.com/ref/harshxu')
    START_TXT = environ.get("START_TXT", '''<b>Hello {} ðð» Im Search Bot I can share Movies and Series ð.</b>

<i>Aá´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´ á´á´ sá´á´ á´Êá´ á´á´É¢Éªá´ á´Ê Êá´á´á´ á´á´Êá´ ÒÊá´á´ á´Êá´ á´á´É´á´ Êá´Êá´á´¡</i>''')
    HELP_TXT = """ð·ð´ð {}
ð·ð´ðð´ ð¸ð ð¼ð ð·ð´ð»ð¿ ð²ð¾ð¼ð¼ð°ð½ð³ð."""
    ABOUT_TXT = """<b><i>ð¤ á´Ê É´á´á´á´ : <a href=https://t.me/FilmHubRobot><b>FilmHub Bot</b></a>\n
ð¨âð» á´á´á´ á´Êá´á´á´Ê : <a href=https://t.me/Harshxubot><b>á´ÊÉªá´á´ Êá´Êá´</b></a>\n
ð Êá´É´É¢á´á´É¢á´ : á´ÊÊá´É¢Êá´á´\n
ð ê°Êá´á´á´á´¡á´Êá´ : á´Êá´Êá´É´ 3\n
ð¡ Êá´sá´á´á´ á´É´ : Êá´Êá´á´á´\n
ð¢ á´á´á´á´á´á´s á´Êá´É´É´á´Ê : <a href=https://t.me/FilmHubUpdates><b></b>á´ÊÉªá´á´ Êá´Êá´</a>\n
ð á´ á´ÊsÉªá´É´ : á´  4.0\n</b></i>"""
    SOURCE_TXT = """<b>Create One Like This:</b>
Â» I will Create One Bot For You<b>
Â» Contact Me @Harshxubot<b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/harshxubot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code>
â ðð¾ðð°ð» ððð´ðð: <code>{}</code>
â ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code>
â ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±
â ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#NewGroup
    
<b>áâº Group âª¼ {}(<code>{}</code>)</b>
<b>áâº Total Members âª¼ <code>{}</code></b>
<b>áâº Added By âª¼ {}</b>
"""
    LOG_TEXT_P = """#NewUser
    
<b>áâº ID - <code>{}</code></b>
<b>áâº Name - {}</b>
"""
