from datetime import datetime

class ChatRoom:
    @staticmethod
    def show_message(user, message):
        print(f"{datetime.now()} [{user.get_name()}] : {message}")

class User:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def send_message(self, message):
        ChatRoom.show_message(self, message)

if __name__ == "__main__":
    robert = User("Robert")
    john = User("John")
    robert.send_message("Hi! John!")
    john.send_message("Hello! Robert!")
