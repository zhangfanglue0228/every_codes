import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox
import sys
import socket
import time
import threading


class Server():
    def __init__(self):
        self.server_window = tk.Tk()
        self.font_style = tkfont.Font(family='Microsoft YaHei UI', size=13)

        # 服务器本地地址
        self.address = ('127.0.0.1', 8000)

        # 初始化服务器
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.address)
        self.server_socket.listen(128)

        # 连接标志
        self.connect_flag = False

    def init_window(self):
        """初始化客户端窗口"""
        self.server_window.title("Python Chat Server")

        # 设置窗口大小为480x520px
        self.server_window.geometry('480x520')

        # 接收消息的listbox框
        self.output_frame = tk.Listbox(self.server_window, width=75, height=18)
        self.output_frame.place(x=10, y=10, anchor='nw')

        # 用于分隔output_frame和input_frame的label
        self.label = tk.Label(self.server_window, text='请输入需要发送的消息：', font=self.font_style,
                              width=18, height=1).place(x=13, y=305, anchor='nw')

        # 接受需要发送的消息的text框
        self.input_frame = tk.Text(self.server_window, width=65, height=10)
        self.input_frame.place(x=10, y=335, anchor='nw')

        # 关闭按钮
        self.close_button = tk.Button(self.server_window, text='关闭', font=self.font_style,
                                      width=8, command=self.close_window)
        self.close_button.place(x=50, y=475, anchor='nw')

        # 发送按钮
        self.send_button = tk.Button(self.server_window, text='发送', font=self.font_style,
                                     width=8, command=self.send_msg)
        self.send_button.place(x=310, y=475, anchor='nw')

    def close_window(self):
        """关闭窗口"""
        sys.exit()

    def recv_msg(self):
        # 提示服务器开启成功
        self.output_frame.insert(tk.END, '服务器已准备就绪！')

        # 持续接受客户端连接
        while True:
            try:
                self.client_socket, connect_address = self.server_socket.accept()
                self.connect_flag = True
                while True:
                    msg_recv = self.client_socket.recv(1024).decode('gbk')
                    if not msg_recv:
                        continue
                    elif msg_recv == 'Success':
                        self.output_frame.insert(tk.END, '服务器与客户端成功建立连接...')
                        self.client_socket.send(b'Success')
                    else:
                        recv_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.output_frame.insert(tk.END, '客户端 ' + recv_time + ':\n')
                        self.output_frame.insert(tk.END, ' ' + msg_recv + '\n')
            except:
                self.output_frame.insert(tk.END, '客户端断开连接...')
                self.connect_flag = False

    def send_msg(self):
        """发送信息"""
        msg_send = self.input_frame.get('1.0', tk.END)
        if msg_send == '\n':
            tkinter.messagebox.showwarning('警告', '发送内容不能为空！')
        else:
            send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.output_frame.insert(tk.END, '服务器 ' + send_time + ':\n')
            self.output_frame.insert(tk.END, ' ' + msg_send + '\n')

            if self.connect_flag:
                self.client_socket.send(msg_send.encode('gbk'))
            else:
                self.output_frame.insert(tk.END, '（未连接客户端，消息发送失败）')

            # 清空output框内内容
            self.input_frame.delete(0.0, msg_send.__len__() - 1.0)

    def start_new_thread(self):
        """启动新线程来接收信息"""
        thread = threading.Thread(target=self.recv_msg, args=())
        thread.setDaemon(True)
        thread.start()
