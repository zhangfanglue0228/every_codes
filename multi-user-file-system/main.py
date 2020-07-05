from element_class import element_class
from operating import *
from admin_oprating import *


def load_all_info():
    info_dict = {}
    with open('user-information.txt', 'r') as f:
        for line in f.readlines():
            user_name = line.rstrip().split()[0] 
            password = line.rstrip().split()[1]
            info_dict[user_name] = password
    return info_dict


def write_all_info(user_info):
    with open('user-information.txt', 'w') as f:
        for key in user_info.keys():
            f.write("%s %s\n" % (key, user_info[key]))


path = 'root'
dir_relationship = {'root': []}
user_info = load_all_info()

clear()
while True:
    # Login
    flag = 1
    print('Please enter your username and password(enter "exit" anywhere to exit system)')
    user_name = input("User name:")
    if user_name == 'exit':
        write_all_info(user_info)
        exit()
    if user_name not in user_info.keys():
        print("User does not exist")
        continue
    password = input("Password:")
    if password == 'exit':
        write_all_info(user_info)
        exit()
    if password == user_info[user_name]:
        print("Login successful")
    else:
        print("The password you entered is wrong, please try again")
        continue
    
    load_user_info(user_name, dir_relationship)
    
    # Pass command
    while True:
        if user_name == 'admin':
            show_terminal(user_name, path)
            command, param = process_command()
            if command == 0 and param == 0:
                continue
            if command == 'help':
                help()
            elif command == 'createusr':
                username = param.split()[0]
                password = param.split()[1]
                createusr(username, password, user_info)
            elif command == 'deleteusr':
                deleteusr(param, user_info)
            elif command == 'changepwd':
                username = param.split()[0]
                password = param.split()[1]
                createusr(username, password, user_info)
            elif command == 'load':
                username = param
                load(path, username, dir_relationship)
            elif command == 'alluser':
                alluser(user_info)
            elif command == 'exit':
                save_user_info(user_name, dir_relationship)
                write_all_info(user_info)
                break
            else:
                print("%s: command not found" % command)

        else:
            show_terminal(user_name, path)
            command, param = process_command()
            if command == 0 and param == 0:
                continue
            if command == 'help':
                help()
            elif command == 'cd':
                path = cd(param, path, dir_relationship)
            elif command == 'mkdir':
                try:
                    authority = int(param.split()[1])
                    param = param.split()[0]
                except:
                    authority = 7
                dir_object = element_class(param, path, authority, 'd')
                mkdir(param, path, dir_object, dir_relationship)
            elif command == 'ls':
                ls(path, dir_relationship)
            elif command == 'll':
                ll(path, dir_relationship)
            elif command == 'create':
                try:
                    authority = int(param.split()[1])
                    param = param.split()[0]
                except:
                    authority = 7
                file_object = element_class(param, path, authority, 'f')
                create(param, path, dir_relationship, file_object)
            elif command == 'write':
                write(param, path, dir_relationship)
            elif command == 'read':
                read(param, path, dir_relationship)
            elif command == 'delete':
                delete(param, path, dir_relationship)
            elif command == 'clear':
                clear()
            elif command == 'exit':
                save_user_info(user_name, dir_relationship)
                # write_all_info(user_info)
                break
            else:
                print("%s: command not found" % command)

