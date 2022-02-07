from random import randint


class User:
    def __init__(self, f_name, l_name):
        self.id = randint(1, 200)
        self.f_name = f_name
        self.l_name = l_name
        self.followers = 0

    def update_f_name(self, f_name):
        self.f_name = f_name

    def follow(self):
        self.followers += 1

    def __str__(self):
        print(self.f_name)


user_1 = User(l_name='Bhagat', f_name='Shashi')

print(user_1.f_name)

user_1.update_f_name("Bhushan")

print(user_1.f_name)
