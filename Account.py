

class Account:
    accounts = []
    magic = b"%Account%:"

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.accounts.append(self)

    def __str__(self):
        return self.name + ":" + self.username + ":" + self.password


def load_accounts(self, file):
    pass

