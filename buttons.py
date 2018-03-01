import utilities as utils
import telegram
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                      ForceReply)

# TODO: Create button menu for feedback choices
toLinks = ['Pages', 'Books', 'Forums', 'MalwareSamples', 'ProjectsAndTools',
           'RSSFeeds', 'SiteLists', 'TwitterLists', 'Subreddits', 'Channels',
           'HandsOn']






def links():
    """ Creates links to report a down link or to submit a new one. """
    
    reply_keyboard = [['Link down', 'New link'],
                      ['Done']]

    return ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)




def menu():
    """ Creates the menu. """
    
    keyboard = [
        [InlineKeyboardButton("Pages",       callback_data='Pages'),
         InlineKeyboardButton("Books",       callback_data='Books')],
        [InlineKeyboardButton("Forums",      callback_data='Forums'),
         InlineKeyboardButton("Samples",     callback_data='MalwareSamples')],
        [InlineKeyboardButton("Tools",       callback_data='ProjectsAndTools'),
         InlineKeyboardButton("RSSFeeds",    callback_data='RSSFeeds')],
        [InlineKeyboardButton("Sites",       callback_data='SiteLists'),
         InlineKeyboardButton("Twitter",     callback_data='TwitterLists')],
        [InlineKeyboardButton("Subreddits",  callback_data='Subreddits'),
         InlineKeyboardButton("TG Channels", callback_data='Channels')],
        [InlineKeyboardButton("Hands On",    callback_data='HandsOn')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    return reply_markup





def parse(bot, update, chat, msg, petition, user):
    if petition in toLinks:
        bot.editMessageText(text=utils.getLinks(petition),
                            chat_id = chat,
                            message_id = msg,
                            disable_web_page_preview=True,
                            reply_markup = menu())


