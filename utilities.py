

def readToken():
    with open('token.txt', 'r') as f:
        return f.readline().strip("\n")
