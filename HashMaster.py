'''
Made by ef71a0518ebc075a7f309cca8
https://github.com/ef71a0518ebc075a7f309cca8
ver 1.0
'''
import hashlib
def guide():
    print("made by ef71a0518ebc075a7f309cca8")
    print("\n\nprompt = what is going to be hashed")
    print("algorithm = hashing algorithm to be used")
    print("only put algorithm name")
    print("dont put any symbols or extra characters")
    print("file output will save your hashes to a file")
    print("you can select whether you are hashing a file")
    print("or hashing text provided though the command line")
    print("or a combination of both")
    print("example: ")
    print("enter a prompt: mypassword")
    print("enter an algorithm: sha3_512\n\n")
def hashgen(vari, fileopac):
    if vari == "Q":
        raise Exception()
    func = input("enter an algorithm: ")
    try:
        hashcod = hashlib.new(func)
        hashcod.update(vari.encode('utf-8'))
        if fileopac:
            fileop.write(hashcod.hexdigest() + "  " + vari + "\n")
        return hashcod.hexdigest()
    except:
        try:
            hashcod.hexdigest(32)
            digestlen = input("enter a digest length: ")
            if fileopac:
                fileop.write(hashcod.hexdigest(int(digestlen)) + "  " + vari + "\n")
            return hashcod.hexdigest(int(digestlen))
        except:
            return "failed"
def filegen(filename, fileopac):
    if filename == "Q":
        raise Exception()
    func = input("enter an algorithm: ")
    try:
        with open(filename, "rb") as fileoper:
            hashinstance = hashlib.file_digest(fileoper, func)
        if fileopac:
            fileop.write(hashinstance.hexdigest() + "  " + filename + "\n")
        return hashinstance.hexdigest()
    except:
        try:
            hashinstance.hexdigest(32)
            digestlen = input("enter a digest length: ")
            if fileopac:
                fileop.write(hashinstance.hexdigest(int(digestlen)) + "  " + filename + "\n")
            return hashinstance.hexdigest(int(digestlen))
        except:
            return "failed"
runtime = True
while True:
    fileopactive = False
    filehashperm = False
    filehashact = True
    if input("want a quick guide? y/n: ") == "y":
        guide()
    if input("do you want to output to a file? y/n:") == "y":
        filepos = input("enter the file path/name: ")
        try:
            fileop = open(filepos, "x")
            fileopactive = True
        except:
            try:
                switch = input("this file already exists!\n append/overwrite: ")
                if switch == "append":
                    fileop = open(filepos, "a")
                    fileopactive = True
                if switch == "overwrite":
                    fileop = open(filepos, "w")
                    fileopactive = True
                else:
                    print("file operation not recognized")
            except:
                print("file operation failed")
                fileopactive = False
    userchoice = input("are you hashing files? only-files(o)/mixed(y)/no-files(n)")
    if userchoice == "o":
        filehashperm = True
        filehashact = False
    elif userchoice == "n":
        filehashact = False
    print(hashlib.algorithms_available)
    while True:
        try:
            if filehashperm:
                    print(filegen(input("\n(Q to restart)\nenter file path/name: "), fileopactive))
            elif filehashact:
                userchoice = input("\n(Q to restart)\nfile(f)/prompt(p): ")
                if userchoice == "f":
                        print(filegen(input("\n(Q to restart)\n\nenter file path/name: "), fileopactive))
                elif userchoice == "p":
                    print(hashgen(input("\n(Q to restart)\n(Q to quit)\n\nenter a prompt: "), fileopactive))
                elif userchoice == "Q":
                    raise Exception()
            else:
                print(hashgen(input("\n(Q to restart)\nenter a prompt: "), fileopactive))
        except:
            if input("\n(all other inputs ignored)\nenter Q again to quit: ") == "Q":
                runtime = False;
            break
    if not runtime:
        break
    print("\n\n\nresetting instance\n\n\n")




#end
