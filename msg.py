# -*- coding: utf-8 -*-
import utilities as utils




#################################################
#               Bot Iniciado                    #
#################################################

infoInit = "Se ha iniciado el bot."




#################################################
#                  /start                       #
#################################################

infoStartBot = """This bot will provide you with resources. 
It's pretty simple, just tap any of the buttons below to get \
a list of links on the topic."""




#################################################
#                   /help                       #
#################################################

infoHelp = """Supported commands:
  /start -> Start the bot
  /help  -> Display this message
  /report -> Report a misbehaving link
  /contribute -> Support us by sending a page or
    subreddit you find useful!
    
"""






#################################################
#                   echo                        #
#################################################

def echo(update):
    chat_id = update.message.chat_id
    name = update.message.from_user.first_name
    msg = update.message.text

    if utils.hasNick(update):
        nick = update.message.from_user.username
        print("\n\nMessage from chat: " + str(chat_id) + " [" + name + "] @" + nick + "\n\t> " + str(msg))
    else:
        print("\n\nMessage from chat: " + str(chat_id) + " [" + name + "] NONICK" + "\n\t> " + str(msg))




#################################################
#                    Unknown                    #
#################################################

infoUnkown = "I'm sorry, I don't recognize that command. Try /help"

unknown = "Comando no reconocido"




#################################################
#                   Information                 #
#################################################

infoInformation = """ Just tap an option!
"""



#################################################
#               InformLinkDown                  #
#################################################

def report(link):
    return "The following link has been reported down: " + link




