import msg

def readToken():
    with open('token.txt', 'r') as f:
        return f.readline().strip("\n")

def hasNick(update):
    if update.message.from_user.username != None:
        return True
    return False

def getLinks(filename):
    links = ""
    count = 1
    fn = 'Resources/' + filename
    
    if filename != 'Books': # El fichero Books es el unico que tiene un formato diferente
        with open(fn, 'r') as f:
            l = f.readline().strip("\n")
            while l:
                links += str(count) + ". " + l + "\n\n"
                count += 1
                l = f.readline().strip("\n")
    else:
        with open(fn, 'r') as f:
            n = f.readline().strip("\n")
            l = f.readline().strip("\n")
            while n and l:
                links+= str(count) + ". " + n + "\n" + l + "\n\n"
                count += 1
                n = f.readline().strip("\n")
                l = f.readline().strip("\n")

    return links

def readAdmins():
    admins = []
    with open('admins.txt', 'r') as f:
        Id = f.readline().strip('\n')
        while Id:
            admins.append(Id)
            Id = f.readline().strip('\n')
    return admins


def isAdmin(user_id):
    admins = readAdmins()
    if user_id in admins:
        return True
    return False

def parseLink(bot, link, option):
    for i in readAdmins():
        if option == "down":
            bot.send_message(chat_id=i, text=msg.reportDown(link))
        elif option == "new":
            bot.send_message(chat_id=i, text=msg.newLink(link))


