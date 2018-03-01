# -*- coding: utf-8 -*-
import utilities as utils
import buttons as butt



#################################################
#               Bot Iniciado                    #
#################################################

infoInit = "Se ha iniciado el bot."




#################################################
#                  /start                       #
#################################################

infoStartBot = """This bot will provide you with resources. 
It's pretty simple, just tap any of the buttons below to get \
a list of links on the topic.
To report useful webs or down links, talk to @QueenNai."""




#################################################
#                   /help                       #
#################################################

infoHelp = """Supported commands:
  /start -> Start the bot
  /help  -> Display this message
  /contribute -> Support us by sending a link \
you found useful or reporting a down link.
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


def option(petition):
    print("\tOpcion: " + str(petition))





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
#               Contribute                      #
#################################################

def reportDown(text):
    link = text.split(" ")[0]
    cat  = text.split(" ")[1]
    utils.removeLink(link, cat)
    return "The link '" + link + "' [" + cat + "] has been reported down."

def newLink(text):
    link = text.split(" ")[0]
    cat  = text.split(" ")[1]
    utils.addLink(link, cat)
    return "The link '" + link + "' [" + cat + "] has been reported as useful." 

whatFor = "You want to report a down link or to provide a new one?"
sendLink = "Nice. Send me the link and the category please!"
reportNotAdmin = "Sorry, but you're not an admin. Message @QueenNai for help."
reportSent = "The contribution has been sent. Thanks for your support!\
\nAnything else you'd like to do?"
reportDone = "Okay, that's it!"




#################################################
#               Files                           #
#################################################

def filesText():
    aux = ""
    for i in butt.toLinks:
        aux += i
        aux += " - "
    return aux
