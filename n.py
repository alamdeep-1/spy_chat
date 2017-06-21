from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Deep Singh', 'Mr.', 20, 6.7)

friend_one = Spy('Vivek', 'Mr.', 20, 5.7)
friend_two = Spy('Gill', 'Mr.', 21, 6.1)
friend_three = Spy('Chawla', 'Dr.', 40, 7.5)


friends = [friend_one, friend_two, friend_three]