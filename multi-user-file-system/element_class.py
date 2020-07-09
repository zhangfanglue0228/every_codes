class element_class():
    def __init__(self, name, path, authority, type_s):
        self.name = name
        self.path = path
        self.content = ''
        self.authority = authority
        self.type = type_s
        self.size = 0


    def write_content(self, usr_content):
        '''更改文件内容'''
        self.content = usr_content

    def change_authority(self, authority_num):
        '''更改文件权限'''
        self.authority = authority_num

    def change_size(self):
        self.size = len(self.content)

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
