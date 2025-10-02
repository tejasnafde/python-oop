class User:
    def __init__(self, username:str, email:str, password:str, greeting:str = None):
        self.username = username
        self.email = email
        self.password = password
        self.greeting = greeting if greeting else None
    def greet_other_user(self, user:'User'):
        if not self.greeting:
            print(f"From {self.username}: Warmest greetings, {user.username}")
        else:
            print(self.greeting,',' ,user.username)


user1 = User('jetasdafne', 'tejas@gmail.com', '1234getonthedancefloor')
user2 = User('timushijoyal', 'mitushi@gmail.com', 'iamawesome2611')
user3 = User('Batman', 'bruce@wayne.org', '******', "I'm BATMAN")

users = [user1,user2, user3]
for i, greeter in enumerate(users):
    for j, receiver in enumerate(users):
        if i == j:
            continue
        greeter.greet_other_user(receiver)
        print("="*30)