# -*- coding: utf-8 -*-

# TODO:
# 1. Añadir el menu con botones
# 2. Añadir la opcion de enviar un feedback o de informar de un link que ya no sirve 
# 3. Añadir la opcion de enviar los PDFs (o links para descargar esos PDFs para evitar
#   problemas)
# 4. Añadir la opcion de seleccionar lenguaje (ingles, castellano o ambos) y enviar
#   solo los pdfs en ese idioma (si es que vamos a enviar PDFs)



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import utilities as utils
import msg

token = utils.readToken()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)






def echo(bot, update):
    """ Manda mensajes de informacion por la pantalla del bot."""

    s = update.message # Para acortar
    msg.echo(update)



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


def Main():

    print(msg.infoInit)

    updater = Updater(token = token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('pages', sendPages))
    dp.add_handler(CommandHandler('rss', sendRSSFeeds))
    dp.add_handler(CommandHandler('samples', sendSamples))
    dp.add_handler(CommandHandler('forums', sendForums))
    dp.add_handler(CommandHandler('tools', sendProjects))
    dp.add_handler(CommandHandler('lists', sendSiteLists))
    dp.add_handler(CommandHandler('twitter', sendTwitterLists))
    dp.add_handler(CommandHandler('books', sendBooks))



    updater.start_polling()
    updater.idle()





if __name__ == "__main__":
    Main()
