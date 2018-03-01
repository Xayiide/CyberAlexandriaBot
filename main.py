# -*- coding: utf-8 -*-

# TODO:
# 2. Añadir la opcion de enviar un feedback o de informar de un link que ya no sirve 
# 3. Añadir la opcion de enviar los PDFs (o links para descargar esos PDFs para evitar
#   problemas)
# 4. Añadir la opcion de seleccionar lenguaje (ingles, castellano o ambos) y enviar
#   solo los pdfs en ese idioma (si es que vamos a enviar PDFs)
# 6. ¿Nueva categoria rollo hackgames (e.g, hackthissite)?

import telegram
from telegram.ext import (Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters,
                          ConversationHandler, RegexHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import utilities as utils
import msg
import buttons as butt  # Yeah, as butt.


token = utils.readToken()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    """ Envia el mensaje de bienvenida. """

    s = update.message

    msg.echo(update)
    bot.send_message(chat_id=s.chat_id, text=msg.infoStartBot, reply_markup=butt.menu())


def help(bot, update):
    """ Envia el mensaje de ayuda. """
    
    s = update.message

    msg.echo(update)
    bot.send_message(chat_id=s.chat_id, text=msg.infoHelp)


def files(bot, update):
    
    s = update.message
    msg.echo(update)
    bot.send_message(chat_id=s.chat_id, text=msg.filesText())





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
    
    msg.option(petition)

    butt.parse(bot, update, chat_id, message, petition, user)





def unknown(bot, update):
    """ Recibe cualquier comando no reconocido e informa de que no existe. """

    s = update.message
    
    msg.echo(update)
    bot.send_message(chat_id=s.chat_id, text=msg.infoUnkown, reply_markup=butt.menu())
    print(msg.unknown)





########################


CHOOSING, TYPING_REPLY = range(2)

option = -1

# TODO: Añadir echos
def contribute(bot, update):

    s = update.message
    if not utils.isAdmin(s.from_user.id):
        update.message.reply_text(msg.reportNotAdmin)
        msg.echo(update)
        
    else:
        update.message.reply_text(msg.whatFor, reply_markup=butt.links())
        msg.echo(update)
        return CHOOSING

def link_down(bot, update):
    update.message.reply_text(msg.sendLink)
    msg.option("Link down")
    global l_option
    l_option = "down"
    return TYPING_REPLY


def new_link(bot, update):
    update.message.reply_text(msg.sendLink)
    msg.option("New Link")
    global l_option
    l_option = "new"
    return TYPING_REPLY

def received_information(bot, update):
    update.message.reply_text(msg.reportSent)
    global l_option
    utils.parseLink(bot, update.message.text, l_option)
    return CHOOSING

def done(bot, update):

    update.message.reply_text(msg.reportDone, reply_markup=ReplyKeyboardRemove())
    msg.option("Done")
    return ConversationHandler.END




def Main():

    print(msg.infoInit)

    updater = Updater(token = token)
    dp = updater.dispatcher


    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('contribute', contribute)],

        states = {
            CHOOSING: [RegexHandler('^Link down$',
                                    link_down,),
                       RegexHandler('^New link$',
                                    new_link),
                       ],

            TYPING_REPLY: [MessageHandler(Filters.text,
                                          received_information),
                          ],
        },

        fallbacks=[RegexHandler('^Done$', done)]
    )






    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('files', files))




    dp.add_handler(CallbackQueryHandler(buttons_handler))

    



    dp.add_handler(conv_handler)
    dp.add_handler(MessageHandler(Filters.command, unknown))

    


    updater.start_polling()
    updater.idle()





if __name__ == "__main__":
    Main()
