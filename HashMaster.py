'''
Made by ef71a0518ebc075a7f309cca8
https://github.com/ef71a0518ebc075a7f309cca8
ver 1.2
'''
import hashlib as hash_library
def guide():
    print("\n\n*        HashMaster        *")
    print("\nmade by ef71a0518ebc075a7f309cca8")
    print("\nprompt = what is going to be hashed")
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
def generate_text_hash(text_prompt, file_output_active):
    if text_prompt == "Q":
        raise Exception()
    algorithm = input("enter an algorithm: ")
    try:
        text_hash_operator = hash_library.new(algorithm)
        text_hash_operator.update(text_prompt.encode('utf-8'))
        if file_output_active:
            file_output_object.write(text_hash_operator.hexdigest() + "  " + text_prompt + "\n")
        return text_hash_operator.hexdigest()
    except:
        try:
            text_hash_operator.hexdigest(32)
            digest_length = input("enter a digest length: ")
            if file_output_active:
                file_output_object.write(text_hash_operator.hexdigest(int(digest_length)) + "  " + text_prompt + "\n")
            return text_hash_operator.hexdigest(int(digest_length))
        except:
            return "failed"
def generate_file_hash(file_input_name, file_output_active):
    if file_input_name == "Q":
        raise Exception()
    algorithm = input("enter an algorithm: ")
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
            digest_length = input("enter a digest length: ")
            if file_output_active:
                file_output_object.write(file_hash_operator.hexdigest(int(digest_length)) + "  " + file_input_name + "\n")
            return file_hash_operator.hexdigest(int(digest_length))
        except:
            return "failed"
execute_loop = True
while execute_loop:
    file_output_active = False
    hash_file_exclusively = False
    hash_file_active = True
    if input("want a quick guide? y/n: ") in ["y", "yes"]:
        guide()
    if input("do you want to output to a file? y/n:") in ["y", "yes"]:
        file_output_name = input("enter the file path/name: ")
        try:
            file_output_object = open(file_output_name, "x")
            file_output_active = True
        except:
            try:
                output_type_switch = input("this file already exists!\n append(a)/overwrite(w): ")
                if output_type_switch in ["append", "a"]:
                    file_output_object = open(file_output_name, "a")
                    file_output_active = True
                if output_type_switch in ["overwrite", "w"]:
                    file_output_object = open(file_output_name, "w")
                    file_output_active = True
                else:
                    print("file operation not recognized")
            except:
                print("file operation failed")
                file_output_active = False
    user_type_input_choice = input("are you hashing files? only-files(o)/mixed(y)/no-files(n)")
    if user_type_input_choice == "o":
        hash_file_exclusively = True
        hash_file_active = False
    elif user_type_input_choice == "n":
        hash_file_active = False
    print("\n" + (", ".join(list(hash_library.algorithms_available))) + "\n")
    while execute_loop:
        try:
            if hash_file_exclusively:
                    print(generate_file_hash(input("\n(Q to restart)\nenter file path/name: "), file_output_active))
            elif hash_file_active:
                user_type_input_choice = input("\n(Q to restart)\nfile(f)/prompt(p): ")
                if user_type_input_choice in ["f", "file"]:
                        print(generate_file_hash(input("\n(Q to restart)\n\nenter file path/name: "), file_output_active))
                elif user_type_input_choice in ["p", "prompt"]:
                    print(generate_text_hash(input("\n(Q to restart)\n(Q to quit)\n\nenter a prompt: "), file_output_active))
                elif user_type_input_choice in ["Q", "quit"]:
                    raise Exception()
            else:
                print(generate_text_hash(input("\n(Q to restart)\nenter a prompt: "), file_output_active))
        except:
            if input("\n(all other inputs ignored)\nenter Q again to quit: ") in ["Q", "quit"]:
                execute_loop = False;
            break
    if execute_loop:
        print("\n\n\nresetting instance\n\n\n")




#end
