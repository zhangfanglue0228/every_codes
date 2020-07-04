import os
from element_class import element_class

def check_file_exists(dir_name, name, dir_relationship):
    for element in dir_relationship[dir_name]:
        if element.name == name:
            return True
    return False


def show_terminal(usr_name, now_path):
    print("%s @ %s$ " % (usr_name, now_path), end='')


def help():
    print("cd : enter a directory; parameter: directory-name")
    print("mkdir : create a directory; parameter: directory-name [user-rights]")
    print("ls : list the simple information of the file or directory in this directory; parameter: None")
    print("ll : ls pro; parameter: None")
    print("create : create a file to write; parameter: file-name [user-rights]")
    print("write : write content in file; parameter: file-name")
    print("read : show the content of the file; parameter:filen-ame")
    print("delete : delete the file; parameter: file or directory-name")
    print("chmod : change the user rights; parameter: file-name user-rights")
    print("clear : clear the terminal")
    print("exit : exit the workspace of current user")


def clear(): os.system('cls')


def exit(): os._exit(0)


def process_command():
    temp_command = input().split()
    if len(temp_command) == 0:
        return 0, 0
    command = temp_command[0]
    temp_command.pop(0)
    param = ' '.join(temp_command)
    return command, param


def cd(param, path, dir_relationship):
    a_path = ''
    path_list = path.split('/')
    if param == '':
        print('Please input directory you want to enter')
        a_path = path
    elif param == '..':  # 返回上一级
        if path == 'root':
            a_path = 'root'
        else:
            path_list.pop()
            a_path = '/'.join(path_list)
    else:
        flag = 0
        for element in dir_relationship[path]:
            if element.name == param:
                if element.type == 'd':
                    a_path = path + '/' + param
                    flag = 1
                    break
                elif element.type == 'f':
                    print("Not a directory")
                    a_path = path
                    flag = 1
                    break
        if flag == 0:
            print("No such file or directory")
            a_path = path
    return a_path


def mkdir(param, path, dir_object, dir_relationship):
    if check_file_exists(path, param, dir_relationship):
        print("File exists")
        return
    dir_relationship[path].append(dir_object)
    dir_relationship[path + '/' + dir_object.name] = []


def ls(path, dir_relationship):
    try:
        for element in dir_relationship[path]:
            print(element.name)
    except:
        return


def ll(path, dir_relationship):
    try:
        print("type\tauthority\tsize\tpath\t\t\tname")
        for element in dir_relationship[path]:
            element.show_element_info()
    except:
        return


def create(param, path, dir_relationship, file_objecet):
    if check_file_exists(path, param, dir_relationship):
        print("File exists")
        return
    dir_relationship[path].append(file_objecet)
    dir_relationship[path + '/' + file_objecet.name] = []
    print("Successfully creat")


def write(param, path, dir_relationship):
    for element in dir_relationship[path]:
        if element.name == param:
            if len(bin(element.authority)[2:]) < 2 or bin(element.authority)[2:][1] != '1':
                print("You have no permission to write this file")
            else:
                print("Enter the content you want to enter: ", end='')
                content = input()
                element.write_content(content)
            return
    print("No such file or directory")



def read(param, path, dir_relationship):
    for element in dir_relationship[path]:
        if element.name == param:
            if bin(element.authority)[2:][0] != '1':
                print("You have no permission to read this file")
            else:
                print("The content of this file: %s" % element.content)
            return
    print("No such file or directory")
    


def delete(param, path, dir_relationship):
    for element in dir_relationship[path]:
        if element.name == param:
            if element.type == 'f':
                dir_relationship[path].pop(dir_relationship[path].index(element))
            elif element.type == 'd':
                dir_relationship.pop(param)
            return
    print("No such file or directory")


def save_user_info(user_name, dir_relationship):
    file_name = 'user-data/' + user_name + '.txt'
    with open(file_name, 'w') as f:
        for key in dir_relationship.keys():
            for element in dir_relationship[key]:
                if element.content == '':
                    content_temp = 'None'
                else:
                    content_temp = '-'.join(element.content.split(' '))
                f.write("%s %s %s %s %s\n" %
                        (element.name, element.path, content_temp, element.authority, element.type))


def load_user_info(user_name, dir_relationship):
    file_name = 'user-data/' + user_name + '.txt'
    try:
        if os.path.getsize(file_name) < 0:
            return
        with open(file_name, 'r') as f:
            for line in f.readlines():
                info_list = line.split()
                element_project = element_class(info_list[0], info_list[1], int(info_list[3]), info_list[4])
                if info_list[2] != 'None':
                    content = ' '.join(info_list[2].split('-'))
                    element_project.write_content(content)
                
                try :
                    dir_relationship[element_project.path].append(element_project)
                except :
                    dir_relationship[element_project.path] = []
                    dir_relationship[element_project.path].append(element_project)
                    dir_relationship[element_project.path + '/' + element_project.name] = []
    except:
        return
