import utilities as utils
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply




def menu():
    """ Creates the menu. """
    
    keyboard = [
        [InlineKeyboardButton("Pages", callback_data='Pages'),
         InlineKeyboardButton("Books", callback_data='Books')],
        [InlineKeyboardButton("Forums", callback_data='Forums'),
         InlineKeyboardButton("Samples", callback_data='MalwareSamples')],
        [InlineKeyboardButton("Tools", callback_data='ProjectsAndTools'),
         InlineKeyboardButton("RSSFeeds", callback_data='RSSFeeds')],
        [InlineKeyboardButton("Sites", callback_data='SiteLists'),
         InlineKeyboardButton("Twitter", callback_data='TwitterLists')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    return reply_markup





def parse(bot, update, chat, msg, petition, user):
    
    toLinks = ['Pages', 'Books', 'Forums', 'MalwareSamples', 'ProjectsAndTools',
               'RSSFeeds', 'SiteLists', 'TwitterLists']

    if petition in toLinks:
        bot.editMessageText(text=utils.getLinks(petition),
                            chat_id = chat,
                            message_id = msg,
                            parse_mode = telegram.ParseMode.MARKDOWN,
                            disable_web_page_preview=True,
                            reply_markup = menu())


