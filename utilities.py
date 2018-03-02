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
    if str(user_id) in admins:
        return True
    return False

def parseLink(bot, text, option):

    if option == "down":
        rep = msg.reportDown(text)
        if rep != None:
            for i in readAdmins():
                bot.send_message(chat_id=i, text=rep)
        else:
            print("\t-- Bad input: " + "[" + text + "]")

    elif option == "new":
        new = msg.newLink(text)
        if new != None:
            for i in readAdmins():
                bot.send_message(chat_id=i, text=new)
        else:
            print("\t-- Bad input: " + "["+ text + "]")



def addLink(link, category):
    try:
        fn = 'Resources/' + category
        with open(fn, 'a') as f:
            f.write(link + '\n')
    except:
        print(msg.wrongData)


def removeLink(link, category):
    try:
        fn = 'Resources/' + category
        old = []
        with open(fn, 'r') as f:
            old = f.readlines()

        new = [i for i in old if i.strip('\n') != link]

        with open(fn, 'w') as f:
            for i in new:
                f.write(i)
    except:
        print(msg.wrongData)
