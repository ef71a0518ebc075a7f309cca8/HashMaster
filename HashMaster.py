'''
Made by ef71a0518ebc075a7f309cca8
ver 1.4
'''
import hashlib as hash_library
import sys as system_integration
def guide():
    print("\n\n*        HashMaster        *")
    print("\nMade by ef71a0518ebc075a7f309cca8")
    print("\nPrompt = what is going to be hashed")
    print("Algorithm = hashing algorithm to be used")
    print("Only put algorithm name")
    print("Dont put any symbols or extra characters")
    print("File output will save your hashes to a file")
    print("You can select whether you are hashing a file")
    print("Or hashing text provided though the command line")
    print("Or a combination of both")
    print("Example: ")
    print("Enter a prompt: mypassword")
    print("Enter an algorithm: sha3_512\n\n")
def generate_text_hash(text_prompt, algorithm, file_output_active):
    if text_prompt == "Q":
        raise Exception()
    if algorithm == "prompt":
        algorithm = input("Enter an algorithm: ")
    try:
        text_hash_operator = hash_library.new(algorithm)
        text_hash_operator.update(text_prompt.encode('utf-8'))
        if file_output_active:
            file_output_object.write(text_hash_operator.hexdigest() + "  " + text_prompt + "\n")
        return text_hash_operator.hexdigest()
    except:
        try:
            text_hash_operator.hexdigest(32)
            digest_length = input("Enter a digest length: ")
            if file_output_active:
                file_output_object.write(text_hash_operator.hexdigest(int(digest_length)) + "  " + text_prompt + "\n")
            return text_hash_operator.hexdigest(int(digest_length))
        except:
            return "failed"
def generate_file_hash(file_input_name, algorithm, file_output_active):
    if file_input_name == "Q":
        raise Exception()
    if algorithm == "prompt":
        algorithm = input("Enter an algorithm: ")
    try:
        file_input_object = open(file_input_name, "rb")
        file_hash_operator = hash_library.new(algorithm)
        while True:
            file_data = file_input_object.read((1024*1024))
            if not file_data:
                break
            file_hash_operator.update(file_data)
        if file_output_active:
            file_output_object.write(file_hash_operator.hexdigest() + "  " + file_input_name + "\n")
        return file_hash_operator.hexdigest()
    except:
        try:
            file_hash_operator.hexdigest(32)
            digest_length = input("Enter a digest length: ")
            if file_output_active:
                file_output_object.write(file_hash_operator.hexdigest(int(digest_length)) + "  " + file_input_name + "\n")
            return file_hash_operator.hexdigest(int(digest_length))
        except:
            return "Failed"
execute_loop = True
file_output_active = False
if len(system_integration.argv) > 1:
    try:
        command_arguments = system_integration.argv[1:]
        argument_dictionary = {
            "alg": False,
            "fil": False,
            "txt": False,
            "out": False,
            "app": False,
            "ovr": False
        }
        for arguments in command_arguments:
            item = arguments.find("=")
            key = arguments[0:item]
            value = arguments[item+1:]
            if argument_dictionary[key] == False:
                argument_dictionary[key] = value
        if argument_dictionary.get("out") != False:
            try:
                file_output_object = open(str(argument_dictionary.get("out"), "x"))
            except:
                if (argument_dictionary.get("ovr") != False) and (argument_dictionary.get("app") != False):
                    raise Exception()
                if argument_dictionary.get("ovr") != False:
                    file_output_object = open(str(argument_dictionary.get("out"), "w"))
                if argument_dictionary.get("app") != False:
                    file_output_object = open(str(argument_dictionary.get("out"), "a"))
                else:
                    print("\nfile already exists! define append or overwrite to output\n")
                    raise Exception()
            if argument_dictionary.get("txt") != False:
                print(generate_text_hash(str(argument_dictionary.get("txt")), str(argument_dictionary.get("alg")), True))
            if argument_dictionary.get("fil") != False:
                print(generate_file_hash(str(argument_dictionary.get("fil")), str(argument_dictionary.get("alg")), True))
        if argument_dictionary.get("txt") != False:
            print(generate_text_hash(str(argument_dictionary.get("txt")), str(argument_dictionary.get("alg")), False))
        if argument_dictionary.get("fil") != False:
            print(generate_file_hash(str(argument_dictionary.get("fil")), str(argument_dictionary.get("alg")), False))
    except:
        print("failed")
        print("syntax: HashMaster.py <option>=<argument> +~ \n")
        print("options: alg=<algorithm> fil=<fileinput> txt=<textinput>\n")
        print("        out=<fileoutput> app=<append>    ovr=<overwrite>\n")
        print("WARNING do not use append and overwite at the same time\n")
    execute_loop = False
while execute_loop:
    file_output_active = False
    hash_file_exclusively = False
    hash_file_active = True
    if input("Want a quick guide? y/n: ") in ["y", "yes"]:
        guide()
    if input("Do you want to output to a file? y/n:") in ["y", "yes"]:
        file_output_name = input("Enter the file path/name: ")
        try:
            file_output_object = open(file_output_name, "x")
            file_output_active = True
        except:
            try:
                output_type_switch = input("This file already exists!\n append(a)/overwrite(w): ")
                if output_type_switch in ["append", "a"]:
                    file_output_object = open(file_output_name, "a")
                    file_output_active = True
                if output_type_switch in ["overwrite", "w"]:
                    file_output_object = open(file_output_name, "w")
                    file_output_active = True
                else:
                    print("File operation not recognized")
            except:
                print("File operation failed")
                file_output_active = False
    user_type_input_choice = input("Are you hashing files? only-files(o)/mixed(y)/no-files(n)")
    if user_type_input_choice == "o":
        hash_file_exclusively = True
        hash_file_active = False
    elif user_type_input_choice == "n":
        hash_file_active = False
    print("\n" + (", ".join(list(hash_library.algorithms_available))) + "\n")
    while execute_loop:
        try:
            if hash_file_exclusively:
                    print(generate_file_hash(input("\n(Q to restart)\nEnter file path/name: "), "prompt", file_output_active))
            elif hash_file_active:
                user_type_input_choice = input("\n(Q to restart)\nfile(f)/prompt(p): ")
                if user_type_input_choice in ["f", "file"]:
                        print(generate_file_hash(input("\n(Q to restart)\n\nEnter file path/name: "), "prompt", file_output_active))
                elif user_type_input_choice in ["p", "prompt"]:
                    print(generate_text_hash(input("\n(Q to restart)\n(Q to quit)\n\nEnter a prompt: "), "prompt", file_output_active))
                elif user_type_input_choice in ["Q", "quit"]:
                    raise Exception()
            else:
                print(generate_text_hash(input("\n(Q to restart)\nEnter a prompt: "), "prompt", file_output_active))
        except:
            if input("\n(all other inputs ignored)\nenter Q again to quit: ") in ["Q", "quit"]:
                execute_loop = False;
            break
    if execute_loop:
        print("\n\n\nresetting instance\n\n\n")




#end
