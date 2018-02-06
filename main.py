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
    
    print("\tOpcion: " + str(petition))

    butt.parse(bot, update, chat_id, message, petition, user)





def unknown(bot, update):
    """ Recibe cualquier comando no reconocido e informa de que no existe. """

    s = update.message
    
    msg.echo(update)
    bot.send_message(chat_id=s.chat_id, text=msg.infoUnkown, reply_markup=butt.menu())
    print(msg.unknown)





########################


CHOOSING, TYPING_REPLY = range(2)


def contribute(bot, update):
    update.message.reply_text(msg.whatFor, reply_markup=butt.links())

    return CHOOSING

def link_down(bot, update, user_data):
    update.message.reply_text(msg.sendLink)
    # TODO: Llamar a funcion linkdown(link) de utils
    return TYPING_REPLY

def new_link(bot, update, user_data):
    update.message.reply_text(msg.sendLink)
    # TODO: llamar a funcion newlink(link) de utils
    return TYPING_REPLY

def received_information(bot, update, user_data):
    update.message.reply_text(msg.reportSent)
                              
    return CHOOSING

def done(bot, update, user_data):

    update.message.reply_text(msg.reportDone, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END







def Main():

    print(msg.infoInit)

    updater = Updater(token = token)
    dp = updater.dispatcher


    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('contribute', contribute)],

        states = {
            CHOOSING: [RegexHandler('^Link down$',
                                    link_down,
                                    pass_user_data=True),
                       RegexHandler('^New link$',
                                    new_link,
                                    pass_user_data=True),
                       ],

            TYPING_REPLY: [MessageHandler(Filters.text,
                                          received_information,
                                          pass_user_data=True),
                          ],
        },

        fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
    )






    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))





    dp.add_handler(CallbackQueryHandler(buttons_handler))

    



    dp.add_handler(conv_handler)
    dp.add_handler(MessageHandler(Filters.command, unknown))

    


    updater.start_polling()
    updater.idle()





if __name__ == "__main__":
    Main()
