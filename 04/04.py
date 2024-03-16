class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        print(f"{self.name} sends a message to {user.name}: {message}")

    def post(self, message):
        print(f"{self.name} posts: {message}")

    def info(self):
        return ""

    def describe(self):
        print(f"{self.name}: {self.info()}")

class Person(User):
    def __init__(self, name, birthdate):
        super().__init__(name)
        self.birthdate = birthdate

    def info(self):
        return f" Дата рождения: {self.birthdate}"

    def subscribe(self, user):
        print(f"{self.name} subscribes to {user.name}")

class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f" Описание: {self.description}"