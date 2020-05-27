from client import Client


def main():
    py_chat_client = Client()
    py_chat_client.init_window()
    py_chat_client.start_new_thread()
    py_chat_client.client_window.mainloop()


if __name__ == '__main__':
    main()
