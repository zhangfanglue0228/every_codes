import os
from operating import *


def help():
    print("createusr: create a user;                parameter: username passward")
    print("deleteusr: delete a user;                parameter: username")
    print("changepwd: change a user's password;     parameter: username new-password")
    print("alluser: show all users' information")


def createusr(user_name, password, user_info):
    if user_name in user_info.keys():
        print("The user you want to create is already in the user list")
        return
    user_info[user_name] = password


def deleteusr(user_name, user_info):
    if user_name not in user_info.keys():
        print("The user you want to delete is not in the user list")
        return
    try:
        file_name = 'user-data/' + user_name + '.txt'
        os.remove(file_name)
    except:
        pass
    user_info.pop(user_name)


def changepwd(user_name, password, user_info):
    if user_name not in user_info.keys():
        print("The user you want to change password is not in the user list")
        return
    user_info[user_name] = password


def alluser(user_info):
    print("user name\t\tpassward")
    for key in user_info.keys():
        print("%s\t\t\t%s" % (key, user_info[key]))


def chmod(authority, param, path, dir_relationship):
    for element in dir_relationship[path]:
        if element.name == param:
            if element.type == 'f':
                element.change_authority(authority)
            else:
                print("This is not a file, you can't change its authority")
            return
    print("No such file or directory")


def load(path, user_name, dir_relationship):
    load_user_info(user_name, dir_relationship)
    username = 'admin@' + user_name
    while True:
        show_terminal(username, path)
        command, param = process_command()
        if command == 0 and param == 0:
                continue
        if command == 'cd':
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
        elif command == 'chmod':
            authority = int(param.split()[1])
            param = param.split()[0]
            chmod(authority, param, path, dir_relationship)
        elif command == 'clear':
            clear()
        elif command == 'exit':
            save_user_info(user_name, dir_relationship)
            break
        else:
            print("%s: command not found" % command)
        

