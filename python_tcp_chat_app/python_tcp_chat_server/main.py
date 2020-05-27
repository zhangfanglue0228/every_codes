from server import Server


def main():
    py_chat_server = Server()
    py_chat_server.init_window()
    py_chat_server.start_new_thread()
    py_chat_server.server_window.mainloop()


if __name__ == '__main__':
    main()
