# -*- coding: utf-8 -*-
from telegram.ext import Updater, commandHandler, MessageHandler, Filters
import logging
import utilities as utils


token = utils.readToken()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)









def Main():

    updater = Updater(token = token)
    dp = updater.dispatcher




    updater.start_polling()
    updater.idle()





if __name__ == "__main__":
    Main()
