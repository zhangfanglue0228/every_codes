class element_class():
    def __init__(self, name, path, authority, type_s):
        self.name = name
        self.path = path
        self.content = ''
        self.authority = authority
        self.type = type_s
        self.size = len(self.content)

    def add_path(self, path_2_add):
        '''文件路径增加'''
        self.path = self.path + path_2_add

    def less_path(self, path_2_less):
        '''文件路径减少'''
        self.path.replace(path_2_less, '')

    # def show_path(self):
    #     '''展示文件路径'''
    #     print(self.path)

    def clear_content(self):
        '''清除文件内容'''
        self.content = ''

    def write_content(self, usr_content):
        '''更改文件内容'''
        self.content = usr_content

    def change_authority(self, authority_num):
        '''更改文件权限'''
        self.authority = authority_num

    def show_element_info(self):
        authority_dict = {
            0: '---',
            1: '--x',
            2: '-w-',
            3: '-wx',
            4: 'r--',
            5: 'r-x',
            6: 'rw-',
            7: 'rwx',
        }
        print("%s\t%s\t\t%s\t%s\t\t\t%s" %
              (self.type, authority_dict[self.authority], self.size, self.path, self.name))
