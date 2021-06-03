from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.telegram_helper.message_utils import *
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.bot_utils import new_thread
from bot import dispatcher
 
 
@new_thread
def cloneNode(update,context):
    args = update.message.text.split(" ",maxsplit=1)
    if update.message.from_user.username:
        uname = f"@{update.message.from_user.username}"
    else:
        uname = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}</a>'
    if uname is not None:
            cc = f'\n\n<b>👤 Uploader: </b>👉 {uname}\n\n▫️#Cloned To Team Drive ✓ \n\n⛔ 𝘿𝙤 𝙣𝙤𝙩 𝙨𝙝𝙖𝙧𝙚 𝙄𝙣𝙙𝙚𝙭 𝙇𝙞𝙣𝙠🙂 \n\n🛡️𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆: <b>@TGFilmZone</b>'
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"𝘾𝙡𝙤𝙣𝙞𝙣𝙜...𝙬𝙖𝙞𝙩 𝙥𝙡𝙯.\n\n<b>Link:</b> <code>{link}</code>",context.bot,update)
        gd = GoogleDriveHelper()
        result, button = gd.clone(link)
        deleteMessage(context.bot,msg)
        if button == "":
            sendMessage(result,context.bot,update)
        else:
            sendMarkup(result + cc,context.bot,update,button)
    else:
        sendMessage("Dammnn 😒😐 \nProvide Google Drive Shareable Link For Clone 🌝\n\n📢 𝐄𝐱𝐚𝐦𝐩𝐥𝐞:\n <code>/clone your Google drive Link</code>\n\n💡 For More Help Join Support Group\n 📨 @MaxxBotChat",context.bot,update)
 
clone_handler = CommandHandler(BotCommands.CloneCommand,cloneNode,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(clone_handler)
