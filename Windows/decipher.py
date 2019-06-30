import sys
try:
    import os
except:
    print("Fatal error: Can not load module \"os\"")
    sys.exit(1)
try:
    import hashlib
except:
    print("Fatal error: Can not load module \"hashlib\"")
    sys.exit(1)
try:
    from termcolor import colored
except:
    try:
        os.system("pip install termcolor")
        from termcolor import colored
    except:
        print("Program has been stopped")
        sys.exit(1)
try:
    from colorama import init
except:
    try:
        os.system("pip install colorama")
        from colorama import init
    except:
        print("Program has been stopped")
        sys.exit(1)
global hashV
global dictU
global tp
global passwd
global tph
global colvo_errors
global limit_errors
init()
limit_errors = 5
colvo_errors = 0
tph = "false"
tp = "false"
defDict = [
    'password',
    'password1',
    'password12',
    'password123',
    'password1234',
    'qwerty',
    'iloveyou',
    'admin',
    'administrator',
    'admin123',
    'abc123',
    'abcd1234',
    '1q2w3e',
    '1q2w3e4r',
    '1q2w3e4r5t',
    'q1q1q1',
    '!@#$%^&*',
    'aa123456',
    'qwerty123',
    '123qweqwe123',
    'passw0rd',
    'qazwsx',
    'zxcvbn',
    'qwaszx',
    'qazwsxedc',
    'qwertyuiop',
    'asdfgh',
    'asdfghjkl',
    'test',
    'killer',
    'root',
    'pass',
    'master',
    'fuckyou',
    'internet',
    '12345',
    '123456',
    '1234567',
    '12345678',
    '123456789',
    '987654321',
    '1234554321',
    '111222',
    '123123',
    '654321',
    '121212',
    '131313',
    '123123123',
    '121314',
    '123789',
    '112233',
    '111111',
    '222222',
    '55555',
    '666666',
    '000000'
]
def force_quit(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print("Program has been stopped")
    else:
        sys.__excepthook__(exctype, value, traceback)
sys.excepthook = force_quit
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(colored("Examples: decipher [hash/file] [dictionary]\nIf you do not specify a dictionary, the default dictionary will be used.","white",attrs=['bold']))
        sys.exit(1)
    if len(sys.argv) == 2:
        if len(sys.argv[1]) != 32 and os.path.exists(sys.argv[1]) != True:
            print(colored("Examples: decipher [hash/file] [dictionary]\nIf you do not specify a dictionary, the default dictionary will be used.","white",attrs=['bold']))
            sys.exit(1)
        elif len(sys.argv[1]) == 32:
            hashV = sys.argv[1]
            tp = "true"
        elif os.path.exists(sys.argv[1]):
            hashV = open(sys.argv[1],"r")
            hashV = hashV.read().split("\n")
            hashV = [x.strip(" ") for x in hashV]
            hashV = [x.strip("\n") for x in hashV]
            tp = "true"
            tph = "true"
        else:
            print(colored("Examples: decipher [hash/file] [dictionary]\nIf you do not specify a dictionary, the default dictionary will be used.","white",attrs=['bold']))
            sys.exit(1)
    elif len(sys.argv) == 3:
        if len(sys.argv[1]) != 32 and os.path.exists(sys.argv[1]) != True:
            print(colored("Examples: decipher [hash/file] [dictionary]\nIf you do not specify a dictionary, the default dictionary will be used.","white",attrs=['bold']))
            sys.exit(1)
        elif len(sys.argv[1]) == 32:
            hashV = sys.argv[1]
        elif os.path.exists(sys.argv[1]):
            hashV = open(sys.argv[1],"r")
            hashV = hashV.read().split("\n")
            hashV = [x.strip(" ") for x in hashV]
            hashV = [x.strip("\n") for x in hashV]
            tph = "true"
        else:
            print(colored("Examples: decipher [hash/file] [dictionary]\nIf you do not specify a dictionary, the default dictionary will be used.","white",attrs=['bold']))
            sys.exit(1)
        if os.path.exists(sys.argv[2]) != True:
            print(colored("Examples: decipher [hash/file] [dictionary]\nIf you do not specify a dictionary, the default dictionary will be used.","white",attrs=['bold']))
            sys.exit(1)
        elif os.path.exists(sys.argv[2]):
            dictU = open(sys.argv[2],"r")
            dictU = dictU.read().split("\n")
if tp == "false":
    if tph == "false":
        for password in dictU:
            passwd = password
            h2 = hashlib.md5(password.encode("utf-8"))
            if hashV == h2.hexdigest():
                print(colored(hashV + ": KEY FOUND! ["+passwd+"]","white","on_green",attrs=['bold']))
                sys.exit(0)
        print(colored(hashV + ": KEY NOT FOUND :(","white","on_red",attrs=['bold']))
    else:
        for hashh in hashV:
            status = False
            if colvo_errors == limit_errors:
                print(colored("\n"+sys.argv[1]+": FILE DOES NOT CONTAIN HASH's!\nProgram has been stopped","white","on_red",attrs=['bold']))
                sys.exit(1)
            if len(hashh) <= 1:
                continue
            if len(hashh) != 32:
                print(colored(hashh + ": THIS IS NOT HASH!","white","on_red",attrs=['bold']))
                colvo_errors = colvo_errors + 1
                continue
            for password in dictU:
                passwd = password
                h2 = hashlib.md5(password.encode("utf-8"))
                if hashh == h2.hexdigest():
                    print(colored(hashh + ": KEY FOUND! ["+passwd+"]","white","on_green",attrs=['bold']))
                    status = True
            if status == False:
                print(colored(hashh + ": KEY NOT FOUND :(","white","on_red",attrs=['bold']))
elif tp == "true":
    if tph == "false":
        for password in defDict:
            passwd = password
            h2 = hashlib.md5(password.encode("utf-8"))
            if hashV == h2.hexdigest():
                print(colored(hashV + ": KEY FOUND! ["+passwd+"]","white","on_green",attrs=['bold']))
                sys.exit(0)
        print(colored(hashV + ": KEY NOT FOUND :(","white","on_red",attrs=['bold']))
    else:
        for hashh in hashV:
            status = False
            if colvo_errors == limit_errors:
                print(colored("\n"+sys.argv[1]+": FILE DOES NOT CONTAIN HASH's!\nProgram has been stopped","white","on_red",attrs=['bold']))
                sys.exit(1)
            if len(hashh) <= 1:
                continue
            if len(hashh) != 32:
                print(colored(hashh + ": THIS IS NOT HASH!","white","on_red",attrs=['bold']))
                colvo_errors = colvo_errors + 1
                continue
            for password in defDict:
                passwd = password
                h2 = hashlib.md5(password.encode("utf-8"))
                if hashh == h2.hexdigest():
                    print(colored(hashh + ": KEY FOUND! ["+passwd+"]","white","on_green",attrs=['bold']))
                    status = True
            if status == False:
                print(colored(hashh + ": KEY NOT FOUND :(","white","on_red",attrs=['bold']))
sys.exit(0)
