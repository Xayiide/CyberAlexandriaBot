# -*- coding: utf-8 -*-
import utilities as utils




#################################################
#               Bot Iniciado                    #
#################################################

infoInit = "Se ha iniciado el bot."




#################################################
#                  /start                       #
#################################################

infoStartBot = """This bot will provide you with resources."""




#################################################
#                   echo                        #
#################################################

def echo(update):
    chat_id = update.message.chat_id
    name = update.message.from_user.first_name
    msg = update.message.text

    if utils.hasNick(update):
        nick = update.message.from_user.username
        print("\n\nMessage from chat: " + str(chat_id) + " from: " + name + " aka: @" + nick + "\n\t> " + str(msg))
    else:
        print("\n\nMessage from chat: " + str(chat_id) + " from: " + name + " aka: NONICK" + "\n\t> " + str(msg))



