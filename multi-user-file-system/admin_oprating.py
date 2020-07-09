import os
from operating import *


def createuser(user_name, password, user_info):
    '''创建一个新的用户'''
    if user_name in user_info.keys():
        print("The user you want to create is already in the user list")
        return
    user_info[user_name] = password


def deleteuser(user_name, user_info):
    '''删除一个用户（取消该用户对文件系统的访问权）'''
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
    '''更改指定用户的登录密码'''
    if user_name in user_info.keys():
        user_info[user_name] = password
        return
    print("The user you want to change its passward is not in user list")


def alluser(user_info):
    '''列出所有用户的用户名和密码'''
    print("user name\t\tpassward")
    for key in user_info.keys():
        print("%s\t\t\t%s" % (key, user_info[key]))


def chmod(authority, param, path, dir_relationship):
    '''更改指定用户的指定文件的读、写、执行权限'''
    for element in dir_relationship[path]:
        if element.name == param:
            if element.type == 'f':
                element.change_authority(authority)
            else:
                print("This is not a file, you can't change its authority")
            return
    print("No such file or directory")


def load(path, user_name):
    '''加载指定用户的文件系统，对其内容进行操作'''
    dir_relationship = {'root': []}
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
        

