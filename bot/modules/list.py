from telegram.ext import CommandHandler, run_async
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot import LOGGER, dispatcher
from bot.helper.telegram_helper.message_utils import sendMessage, sendMarkup, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
import threading
from bot.helper.telegram_helper.bot_commands import BotCommands

@run_async
def list_drive(update,context):
    try:
        search = update.message.text.split(' ',maxsplit=1)[1]
        LOGGER.info(f"Searching: {search}")
        reply = sendMessage('𝙎𝙚𝙖𝙧𝙘𝙝𝙞𝙣𝙜....𝙥𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩!', context.bot, update)
        gdrive = GoogleDriveHelper(None)
        msg, button = gdrive.drive_list(search)

        if button:
            editMessage(msg, reply, button)
        else:
            editMessage('𝙽𝚘 𝚁𝚎𝚜𝚞𝚕𝚝 𝙵𝚘𝚞𝚗𝚍', reply, button)

    except IndexError:
        sendMessage('<b> Opps</b> 🤦 \n\n<b>How to search? </b>\n\n<b>🔎 Example:</b> <code>/find Tron Legacy</code>', context.bot, update)


list_handler = CommandHandler(BotCommands.ListCommand, list_drive,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(list_handler)
