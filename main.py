# -*- coding: utf-8 -*-

# TODO:
# 2. Añadir la opcion de enviar un feedback o de informar de un link que ya no sirve 
# 3. Añadir la opcion de enviar los PDFs (o links para descargar esos PDFs para evitar
#   problemas)
# 4. Añadir la opcion de seleccionar lenguaje (ingles, castellano o ambos) y enviar
#   solo los pdfs en ese idioma (si es que vamos a enviar PDFs)
# 5. Añadir los putos subredditsy todos los links que quedan
# 6. ¿Nueva categoria rollo hackgames (e.g, hackthissite)?

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import utilities as utils
import msg
import buttons as butt  # Yeah, as butt.


token = utils.readToken()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


"""
def menu(bot, chat_id):
    # Creates the menu. 
    keyboard = [
        [InlineKeyboardButton("Pages",    callback_data='Pages'),
         InlineKeyboardButton("Books",    callback_data='Books')],
        [InlineKeyboardButton("Forums",   callback_data='Forums'),
         InlineKeyboardButton("Samples",  callback_data='MalwareSamples')],
        [InlineKeyboardButton("Tools",    callback_data='ProjectsAndTools'),
         InlineKeyboardButton("RSSFeeds", callback_data='RSSFeeds')],
        [InlineKeyboardButton("Sites",    callback_data='SiteLists'),
         InlineKeyboardButton("Twitter",  callback_data='TwitterLists')]
    ]


    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, reply_)
   # update.message.reply_text("What are you looking for?", reply_markup=reply_markup)
"""




def echo(bot, update):
    """ Manda mensajes de informacion por la pantalla del bot."""

    s = update.message # Para acortar
    msg.echo(update)


def start(bot, update):
    """ Envia el mensaje de bienvenida. """

    s = update.message
    bot.send_message(chat_id=s.chat_id, text=msg.infoStartBot)
    butt.menu(bot, s.chat_id)



def help(bot, update):
    """ Envia un mensaje de ayuda al usuario. """

    s = update.message
    bot.send_message(chat_id=s.chat_id, text=msg.infoHelpBot)


def sendPages(bot, update):
    """ Envia un mensaje con la lista de links. """

    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=utils.getLinks('Pages'))


def sendRSSFeeds(bot, update):
    """ Envia un mensaje con la lista de links a Feeds RSS. """

    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=utils.getLinks('RSSFeeds'))


def sendSamples(bot, update):
    """ Envia una lista de sitios donde descargar muestras 
        de malware. """
    
    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=utils.getLinks('MalwareSamples'))


def sendForums(bot, update):
    """ Envia una lista de foros. """

    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=utils.getLinks('Forums'))


def sendProjects(bot, update):
    """ Envia una lista de proyectos y herramientas. """

    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=utils.getLinks('ProjectsAndTools'))


def sendSiteLists(bot, update):
    """ Envia una lista de sitios que contienen mas sitios (?). """
    
    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=utils.getLinks('SiteLists'))


def sendTwitterLists(bot, update):
    """ Envia una lista de listas de twitter. """

    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=utils.getLinks('TwitterLists'))

def sendBooks(bot, update):
    """ Envia una lista de libros buenos. """

    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=utils.getLinks('Books'))





###############
#   Botones   #
###############

def buttons_handler(bot, update):
    """ Crea el menu de botones. """

    query    = update.callback_query

    message  = query.message.message_id
    petition = query.data
    chat_id  = query['message']['chat']['id']
    user     = query['message']['chat']['first_name']
    
    print("\tUsuario: " + str(user) + " [" + str(chat_id) + "]")
    print("\tOpcion: " + str(petition))

    butt.parse(bot, update, chat_id, message, petition, user)



"""
    bot.edit_message_text(text=utils.getLinks(petition),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
"""


def unknown(bot, update):
    """ Recibe cualquier comando no reconocido e informa de que no existe. """

    s = update.message
    
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=msg.infoUnkown)
    print(msg.unknown)


def information(bot, update):
    """ Recibe un mensaje cualquiera (no comando) y manda instrucciones
        para el bot. """

    s = update.message
    echo(bot, update)
    bot.send_message(chat_id=s.chat_id, text=msg.infoInformation)


def reportDown(bot, update):
    pass




def Main():

    print(msg.infoInit)

    updater = Updater(token = token)
    dp = updater.dispatcher


    dp.add_handler(MessageHandler(Filters.text, information))
    dp.add_handler(CommandHandler('pages', sendPages))
    dp.add_handler(CommandHandler('rss', sendRSSFeeds))
    dp.add_handler(CommandHandler('samples', sendSamples))
    dp.add_handler(CommandHandler('forums', sendForums))
    dp.add_handler(CommandHandler('tools', sendProjects))
    dp.add_handler(CommandHandler('lists', sendSiteLists))
    dp.add_handler(CommandHandler('twitter', sendTwitterLists))
    dp.add_handler(CommandHandler('books', sendBooks))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))


#    dp.add_handler(CommandHandler('menu', menu))
    dp.add_handler(CallbackQueryHandler(buttons_handler))

    dp.add_handler(MessageHandler(Filters.command, unknown))

    


    updater.start_polling()
    updater.idle()





if __name__ == "__main__":
    Main()
