import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox
import sys
import time
import socket
import threading


class Client():
    """客户端类"""

    def __init__(self):
        self.client_window = tk.Tk()
        self.font_style = tkfont.Font(family='Microsoft YaHei UI', size=13)
        
        # 服务器地址
        self.server_address = ('127.0.0.1', 8000)

        # 链接标志
        self.connect_flag = False

    def init_window(self):
        """初始化客户端窗口"""
        self.client_window.title("Python Chat Client")

        # 设置窗口大小为480x520px
        self.client_window.geometry('480x520')

        # 接收消息的listbox框
        self.output_frame = tk.Listbox(self.client_window, width=75, height=18)
        self.output_frame.place(x=10, y=10, anchor='nw')

        # 用于分隔output_frame和input_frame的label
        self.label = tk.Label(self.client_window, text='请输入需要发送的消息：', font=self.font_style,
                              width=18, height=1).place(x=13, y=305, anchor='nw')

        # 接受需要发送的消息的text框
        self.input_frame = tk.Text(self.client_window, width=65, height=10)
        self.input_frame.place(x=10, y=335, anchor='nw')

        # 关闭按钮
        self.close_button = tk.Button(self.client_window, text='关闭', font=self.font_style,
                                      width=8, command=self.close_window)
        self.close_button.place(x=50, y=475, anchor='nw')

        # 发送按钮
        self.send_button = tk.Button(self.client_window, text='发送', font=self.font_style,
                                     width=8, command=self.send_msg)
        self.send_button.place(x=310, y=475, anchor='nw')

    def close_window(self):
        """关闭窗口"""
        sys.exit()

    def send_msg(self):
        """发送信息"""
        msg_send = self.input_frame.get('1.0', tk.END)
        if msg_send == '\n':
            tkinter.messagebox.showwarning('警告', '发送内容不能为空！')
        else:
            send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.output_frame.insert(tk.END, '客户端 ' + send_time + ':\n')
            self.output_frame.insert(tk.END, ' ' + msg_send)

            if self.connect_flag:
                self.client_socket.send(msg_send.encode('gbk'))
            else:
                self.output_frame.insert(tk.END, '（未连接服务器，消息发送失败...\n）')

            # 清空output框内内容
            self.input_frame.delete(0.0, msg_send.__len__() - 1.0)

    def recv_msg(self):
        self.output_frame.insert(tk.END, '连接服务器中...')

        # 客户端连接服务器
        while True:
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect(self.server_address)
                self.connect_flag = True
                # 连接成功向服务器发送成功标志'Success'
                self.client_socket.send(b'Success')
                # 连接成功后开始接收服务器信息
                while True:
                    msg_recv = self.client_socket.recv(1024).decode('gbk')
                    if msg_recv == 'Success':
                        self.output_frame.insert(tk.END, '客户端已与服务器成功建立连接...')
                    elif msg_recv == 'Fail':
                        self.output_frame.insert(tk.END, '客户端与服务器建立连接失败...')
                    elif not msg_recv:
                        continue
                    else:
                        recv_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.output_frame.insert(tk.END, '服务器 ' + recv_time + ':\n')
                        self.output_frame.insert(tk.END, ' ' + msg_recv + '\n')
            except:
                # 连接失败标志设为False
                self.connect_flag = False

    def start_new_thread(self):
        """启动新线程来接收信息"""
        thread = threading.Thread(target=self.recv_msg, args=())
        thread.setDaemon(True)
        thread.start()
